# Kaggle Notebooks

This folder contains 3 ready-to-run Kaggle notebooks for microplastics detection.

---

## Available Notebooks

### 1. U-Net Segmentation (START HERE!)
**File**: `kaggle_unet_microplastics.ipynb`

- **Task**: Pixel-level segmentation
- **Output**: Binary masks (microplastic vs background)
- **Time**: 20-30 minutes
- **Difficulty**: Beginner-friendly

**How to use**:
1. Upload to Kaggle
2. Add microplastic dataset
3. Update `DATASET_PATH` in cell 2
4. Click "Run All"

---

### 2. YOLOv5 Detection
**File**: `kaggle_yolov5_microplastics.ipynb`

- **Task**: Object detection
- **Output**: Bounding boxes + counts
- **Time**: 40-60 minutes
- **Difficulty**: Intermediate

**How to use**:
1. Upload to Kaggle
2. Add microplastic dataset
3. Update `DATASET_PATH` in cell 2
4. Click "Run All"

---

### 3. SSD Classification
**File**: `kaggle_ssd_classification.ipynb`

- **Task**: Classification + analysis
- **Output**: 4 categories + 17 parameters
- **Time**: N/A (use web interface)
- **Difficulty**: Advanced

**Easiest option**: Use web interface at https://research-segmentation.toc.yt

---

## Quick Start

### Step 1: Go to Kaggle
https://www.kaggle.com/code

### Step 2: Create New Notebook
Click "New Notebook" → "Upload Notebook"

### Step 3: Select File
Choose one of the notebooks above (start with U-Net)

### Step 4: Add Dataset
Click "+ Add Data" (right panel)

**Option A**: Search for existing datasets
- Search: "microplastic"
- Popular: `imtkaggleteam/microplastic-dataset-for-computer-vision`

**Option B**: Upload your own
- Upload DeepParticle dataset
- Name it: `microplastics-deepparticle`

### Step 5: Update Path
In the notebook, update `DATASET_PATH`:
```python
DATASET_PATH = "/kaggle/input/your-dataset-name"
```

### Step 6: Run
Click "Run All" or Shift+Enter through cells

---

## Dataset Paths

After adding a dataset to Kaggle, it will be at:
```
/kaggle/input/[dataset-name]/
```

Common structures:
```
# DeepParticle
/kaggle/input/microplastics-deepparticle/
├── MICRO/
│   ├── raw_img/
│   └── annotation/
├── MESO/
└── MACRO/

# Other datasets may have:
/kaggle/input/dataset-name/
├── images/
└── masks/
```

Update the `DATASET_PATH` variable in each notebook to match your dataset structure.

---

## Troubleshooting

### "Dataset not found"
- Verify dataset is added (check right panel)
- Update `DATASET_PATH` to match your dataset name
- Check available datasets: `!ls /kaggle/input/`

### "Out of memory"
- Reduce batch size
- Enable GPU: Settings → Accelerator → GPU T4 x2
- Restart kernel

### "No module named..."
- Notebooks install dependencies automatically
- If error persists, restart kernel

---

## Expected Results

### U-Net
- Training curves (loss, IoU, Dice)
- Predicted segmentation masks
- Metrics: IoU 0.8+, Dice 0.85+

### YOLOv5
- Detection boxes
- Particle counts
- mAP metrics

### SSD
- 4-category classification
- TSV file with 17 parameters
- Detailed particle analysis

---

## Output Location

All results are saved to:
```
/kaggle/working/
├── models/          # Trained models
├── results/         # Plots and visualizations
└── output/          # Export files
```

Download from "Output" tab in Kaggle.

---

## Need Help?

See documentation:
- [QUICK_START.md](../QUICK_START.md) - Step-by-step tutorial
- [DATASETS.md](../DATASETS.md) - Dataset information
- [GET_STARTED.md](../GET_STARTED.md) - Quick reference
- [README.md](../README.md) - Project overview

---

## Tips

1. **Start with U-Net** - Easiest to understand
2. **Use GPU** - Much faster training
3. **Save often** - Kaggle sessions timeout
4. **Version your notebook** - Save checkpoints
5. **Download results** - Don't rely on Kaggle storage

---

**You're ready to start!** Upload a notebook and begin training.
