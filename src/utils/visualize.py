from pathlib import Path
import numpy as np
import cv2


def save_overlay(rgb: np.ndarray, mask: np.ndarray, out_path: Path, alpha: float = 0.4) -> None:
    rgb = rgb.copy()
    if rgb.ndim == 3 and rgb.shape[2] == 3:
        base = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    else:
        base = cv2.cvtColor(rgb, cv2.COLOR_GRAY2BGR)
    mask_bgr = np.zeros_like(base)
    mask_bgr[..., 2] = (mask > 0) * 255  # red overlay
    over = cv2.addWeighted(base, 1.0, mask_bgr, alpha, 0)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_path), over)

