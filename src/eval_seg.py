from __future__ import annotations

from pathlib import Path
import argparse
import torch
from torch.utils.data import DataLoader

from .data.seg_dataset import SegmentationDataset
from .data.transforms import build_valid_tfms
from .models.unet_factory import build_unet
from .utils.metrics import dice_coef, iou


def load_checkpoint(path: Path):
    ckpt = torch.load(path, map_location="cpu")
    return ckpt["model"], ckpt.get("cfg", {})


@torch.no_grad()
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", type=str, default="data/images")
    ap.add_argument("--masks", type=str, default="data/masks")
    ap.add_argument("--checkpoint", type=str, required=True)
    args = ap.parse_args()

    state_dict, cfg = load_checkpoint(Path(args.checkpoint))
    model = build_unet(
        encoder_name=cfg.get("model", {}).get("encoder", "resnet34"),
        encoder_weights=None,
        classes=1,
        activation=None,
    )
    model.load_state_dict(state_dict)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device).eval()

    tfms = build_valid_tfms(tuple(cfg.get("data", {}).get("img_size", [512, 512])))
    ds = SegmentationDataset(args.images, args.masks, transform=tfms)
    dl = DataLoader(ds, batch_size=4, shuffle=False)

    total_dice = 0.0
    total_iou = 0.0
    n_batches = 0
    for images, masks in dl:
        images = images.to(device)
        masks = masks.unsqueeze(1).float().to(device)
        logits = model(images)
        probs = torch.sigmoid(logits)
        total_dice += dice_coef(probs, masks).item()
        total_iou += iou(probs, masks).item()
        n_batches += 1

    print(f"Dice: {total_dice/n_batches:.4f} | IoU: {total_iou/n_batches:.4f}")


if __name__ == "__main__":
    main()

