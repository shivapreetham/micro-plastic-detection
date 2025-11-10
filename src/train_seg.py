from __future__ import annotations

import math
from pathlib import Path
from typing import Tuple

import torch
from torch.utils.data import DataLoader, random_split
import torch.nn.functional as F
from torch import optim

from .config import load_config, parse_args
from .data.seg_dataset import SegmentationDataset
from .data.transforms import build_train_tfms, build_valid_tfms
from .models.unet_factory import build_unet
from .utils.metrics import dice_coef, iou
from .utils.seed import set_seed


def make_loaders(cfg: dict) -> Tuple[DataLoader, DataLoader]:
    data_dir = Path(cfg["data"].get("root", "data"))
    images_dir = data_dir / "images"
    masks_dir = data_dir / "masks"

    img_size = tuple(cfg["data"].get("img_size", [512, 512]))
    train_tfms = build_train_tfms(img_size)
    valid_tfms = build_valid_tfms(img_size)

    full = SegmentationDataset(images_dir, masks_dir, transform=train_tfms)
    val_ratio = float(cfg["train"].get("val_ratio", 0.2))
    val_len = max(1, int(len(full) * val_ratio))
    train_len = len(full) - val_len
    train_set, val_set = random_split(full, [train_len, val_len])

    # attach valid transforms to val subset
    val_set.dataset.transform = valid_tfms

    bs = int(cfg["train"].get("batch_size", 4))
    nw = int(cfg["train"].get("num_workers", 2))
    train_loader = DataLoader(train_set, batch_size=bs, shuffle=True, num_workers=nw)
    val_loader = DataLoader(val_set, batch_size=bs, shuffle=False, num_workers=nw)
    return train_loader, val_loader


def train_one_epoch(model, loader, optimizer, device):
    model.train()
    total_loss = 0.0
    total_dice = 0.0
    for images, masks in loader:
        images = images.to(device)
        masks = masks.unsqueeze(1).float().to(device)

        logits = model(images)
        loss = F.binary_cross_entropy_with_logits(logits, masks) + 0.5 * (1 - dice_coef(torch.sigmoid(logits), masks))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        total_dice += dice_coef(torch.sigmoid(logits), masks).item()
    n = len(loader)
    return total_loss / n, total_dice / n


@torch.no_grad()
def validate(model, loader, device):
    model.eval()
    total_loss = 0.0
    total_dice = 0.0
    total_iou = 0.0
    for images, masks in loader:
        images = images.to(device)
        masks = masks.unsqueeze(1).float().to(device)

        logits = model(images)
        loss = F.binary_cross_entropy_with_logits(logits, masks) + 0.5 * (1 - dice_coef(torch.sigmoid(logits), masks))
        total_loss += loss.item()
        total_dice += dice_coef(torch.sigmoid(logits), masks).item()
        total_iou += iou(torch.sigmoid(logits), masks).item()
    n = len(loader)
    return total_loss / n, total_dice / n, total_iou / n


def main():
    args = parse_args()
    cfg = load_config(args.config)

    seed = int(cfg["train"].get("seed", 42))
    set_seed(seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train_loader, val_loader = make_loaders(cfg)

    model_cfg = cfg["model"]
    model = build_unet(
        encoder_name=model_cfg.get("encoder", "resnet34"),
        encoder_weights=model_cfg.get("encoder_weights", "imagenet"),
        classes=1,
        activation=None,
    ).to(device)

    lr = float(cfg["train"].get("lr", 1e-3))
    wd = float(cfg["train"].get("weight_decay", 1e-5))
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=wd)

    epochs = int(cfg["train"].get("epochs", 30))
    out_dir = Path(cfg["train"].get("out_dir", "models"))
    out_dir.mkdir(parents=True, exist_ok=True)
    best_dice = -math.inf
    best_path = out_dir / "best.ckpt"

    for epoch in range(1, epochs + 1):
        tr_loss, tr_dice = train_one_epoch(model, train_loader, optimizer, device)
        va_loss, va_dice, va_iou = validate(model, val_loader, device)
        print(
            f"Epoch {epoch:03d}/{epochs} | "
            f"train_loss={tr_loss:.4f} train_dice={tr_dice:.4f} | "
            f"val_loss={va_loss:.4f} val_dice={va_dice:.4f} val_iou={va_iou:.4f}"
        )

        if va_dice > best_dice:
            best_dice = va_dice
            torch.save({"model": model.state_dict(), "cfg": cfg}, best_path)
            print(f"Saved best model -> {best_path}")


if __name__ == "__main__":
    main()

