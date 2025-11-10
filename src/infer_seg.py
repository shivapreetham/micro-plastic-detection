from __future__ import annotations

from pathlib import Path
import argparse
import cv2
import numpy as np
import torch

from .data.transforms import build_valid_tfms
from .models.unet_factory import build_unet
from .utils.visualize import save_overlay


def load_checkpoint(path: Path):
    ckpt = torch.load(path, map_location="cpu")
    return ckpt["model"], ckpt.get("cfg", {})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", type=str, required=True, help="Folder of images")
    ap.add_argument("--checkpoint", type=str, required=True, help="Path to best.ckpt")
    ap.add_argument("--out", type=str, default="out_preds", help="Output folder")
    args = ap.parse_args()

    images_dir = Path(args.images)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    state_dict, cfg = load_checkpoint(Path(args.checkpoint))
    model = build_unet(
        encoder_name=cfg.get("model", {}).get("encoder", "resnet34"),
        encoder_weights=None,
        classes=1,
        activation=None,
    )
    model.load_state_dict(state_dict)
    model.eval()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    tfms = build_valid_tfms(tuple(cfg.get("data", {}).get("img_size", [512, 512])))

    for p in sorted(list(images_dir.glob("*.*"))):
        img = cv2.imread(str(p), cv2.IMREAD_COLOR)
        if img is None:
            continue
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        t = tfms(image=rgb)
        x = t["image"].unsqueeze(0).to(device)
        with torch.no_grad():
            logits = model(x)
            prob = torch.sigmoid(logits)[0, 0].cpu().numpy()
        mask = (prob > 0.5).astype(np.uint8) * 255
        save_overlay(rgb, mask, out_dir / f"{p.stem}_overlay.png")
        cv2.imwrite(str(out_dir / f"{p.stem}_mask.png"), mask)
        print(f"Saved {p.name} -> mask + overlay")


if __name__ == "__main__":
    main()

