# Microplastics Detection Project

Strong, reproducible pipeline for microplastics detection and segmentation in images from seawater, marine, beach, and sewage sources. Implements a U-Net family model (via `segmentation-models-pytorch`) with Albumentations, robust training loop, evaluation, and inference utilities.

Paper context: Built with reference to current literature including Frontiers in Environmental Science (2024): 10.3389/fenvs.2024.1386292.

## Project Structure
```
micro-plastic-detection/
├── data/
│   ├── images/                    # Training images (user-provided)
│   ├── masks/                     # Segmentation masks (user-provided)
│   └── raw/                       # Raw downloads before preparation
├── models/                        # Saved checkpoints
├── src/
│   ├── config.py
│   ├── train_seg.py
│   ├── infer_seg.py
│   ├── eval_seg.py
│   ├── data/
│   │   ├── seg_dataset.py
│   │   ├── transforms.py
│   │   └── download_zenodo.py
│   ├── models/
│   │   └── unet_factory.py
│   └── utils/
│       ├── seed.py
│       ├── metrics.py
│       └── visualize.py
├── configs/
│   └── segmentation.yaml          # Default training config
├── notebooks/
│   └── 00_quickstart.ipynb        # Optional walkthrough (coming later)
├── requirements.txt
├── setup.bat                      # Windows setup script (venv + deps)
├── run.bat                        # Example training run
├── DATASETS.md                    # Curated dataset links and notes
└── README.md
```

## Quick Start

### 1) Environment setup (Windows):
- Double-click `setup.bat` or run from `cmd`:
  - `setup.bat`

### 2) Prepare data:
- Download a dataset listed in `DATASETS.md`, then arrange files as:
  - `data/images/<filename>.png|jpg`
  - `data/masks/<filename>.png` (same basenames as images)

### 3) Train
- From an activated venv:
  - `python -m src.train_seg --config configs/segmentation.yaml`

### 4) Inference
- Predict on a folder of images:
  - `python -m src.infer_seg --images data/images --checkpoint models/best.ckpt --out out_preds`

## Notes on Data
- This repo does not redistribute datasets. See `DATASETS.md` for vetted sources (microscopy fluorescence/brightfield, SEM, FTIR-derived 2D exports when available) spanning seawater, beach/marine, and sewage.
- If your dataset differs in format, adjust `src/data/seg_dataset.py` or create a small adapter.

## Dependencies
- PyTorch + torchvision (GPU recommended)
- segmentation-models-pytorch
- Albumentations, OpenCV, Pillow
- scikit-learn, tqdm, matplotlib, seaborn
- pyyaml

Install via `setup.bat` or: `pip install -r requirements.txt`.
