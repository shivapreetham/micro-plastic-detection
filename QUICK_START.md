# Quick Start Guide - Microplastics Detection

Get started with microplastics detection in 3 simple steps!

---

## Step 1: Download Dataset

### Option A: Automated Download (Recommended)

```bash
python download_datasets.py
```

This will download the **DeepParticle dataset** (541 MB) from The Ocean Cleanup.

### Option B: Manual Download

1. Visit: https://figshare.com/ndownloader/files/48254164
2. Save as: `data/DeepParticle.zip`
3. Extract the zip file

---

## Step 2: Upload to Kaggle

### Why Kaggle?
- Free GPU access
- No local setup required
- Cloud storage for datasets
- Easy sharing and collaboration

### How to Upload Dataset

1. **Go to Kaggle Datasets**: https://www.kaggle.com/datasets

2. **Create New Dataset**:
   - Click "New Dataset"
   - Click "Upload" tab

3. **Upload Files**:
   - Drag and drop the extracted `DeepParticle` folder OR
   - For smaller upload, zip just the MICRO folder:
     ```bash
     cd data/DeepParticle
     zip -r microplastics-micro.zip MICRO/
     ```

4. **Set Dataset Info**:
   - **Title**: Microplastics DeepParticle
   - **Slug**: `microplastics-deepparticle`
   - **Description**: Ocean Cleanup microplastics dataset with 4,795 annotated particles

5. **Click "Create"**

---

## Step 3: Run Kaggle Notebooks

### Method 1: U-Net Segmentation (Start Here!)

**Goal**: Pixel-level segmentation of microplastics

1. **Go to**: https://www.kaggle.com/code
2. **Click**: "New Notebook"
3. **Upload**: `notebooks/kaggle_unet_microplastics.ipynb`
4. **Add Data**:
   - Click "+ Add Data" on right panel
   - Search: `microplastics-deepparticle`
   - Click "Add"
5. **Update Path** in cell 4:
   ```python
   DATASET_NAME = "your-username/microplastics-deepparticle"
   IMAGE_DIR = f"/kaggle/input/{DATASET_NAME}/MICRO/raw_img"
   MASK_DIR = f"/kaggle/input/{DATASET_NAME}/MICRO/annotation"
   ```
6. **Click**: "Run All" or press Shift+Enter through cells

**Expected Results**:
- Training curves (loss, IoU, Dice)
- Predicted segmentation masks
- Model saved to `/kaggle/working/models/`

---

### Method 2: YOLOv5 Detection

**Goal**: Detect and count microplastic particles with bounding boxes

1. **Upload**: `notebooks/kaggle_yolov5_microplastics.ipynb`
2. **Add Data**: Same dataset as above
3. **Update** dataset paths
4. **Run All**

**Expected Results**:
- Detection boxes on images
- Particle counts
- Confidence scores

---

### Method 3: SSD Classification

**Goal**: Classify particles into 4 types (hard, pellet, line, foam)

**EASIEST OPTION**: Use Web Interface (No code!)

1. Visit: https://research-segmentation.toc.yt
2. Upload images
3. Download TSV results

**Advanced Option**: Run Kaggle notebook

1. **Upload**: `notebooks/kaggle_ssd_classification.ipynb`
2. **Add Data**: Same dataset
3. **Run All**

**Expected Results**:
- 4-category classification
- 17 physical parameters per particle
- TSV file with results

---

## What to Expect

### Training Time (on Kaggle GPU)

- **U-Net**: ~20-30 minutes (20 epochs)
- **YOLOv5**: ~40-60 minutes (50 epochs)
- **SSD**: Variable (or use pre-trained)

### Results You'll Get

#### Method 1 (U-Net):
- Binary segmentation masks
- IoU, Dice, F1 scores
- Training curves
- Visualizations

#### Method 2 (YOLOv5):
- Bounding boxes
- Detection count per image
- Confidence scores
- mAP metrics

#### Method 3 (SSD):
- Classification (hard/pellet/line/foam)
- 17 parameters: size, color, shape, etc.
- TSV export for analysis

---

## Troubleshooting

### "Dataset not found" Error

**Solution**:
1. Verify dataset name matches in code
2. Check dataset was added to notebook (right panel)
3. Verify path structure

### "Out of memory" Error

**Solution**:
1. Reduce batch size in notebook
2. Enable GPU: Settings → Accelerator → GPU
3. Restart kernel

### "Permission denied" Error

**Solution**:
1. Make dataset public or
2. Use your own Kaggle username in path

---

## Next Steps After Training

### Save Your Model

Models are automatically saved to:
- U-Net: `/kaggle/working/models/best_unet_model.pth`
- YOLOv5: `/kaggle/working/runs/train/weights/best.pt`

Download them by clicking "Output" tab in Kaggle.

### Run Inference on New Images

1. Upload new images to `/kaggle/input/`
2. Load trained model
3. Run prediction cells

### Export Results

Results are saved to:
- `/kaggle/working/results/` (images, plots)
- `/kaggle/working/output/` (CSV, TSV files)

Download from "Output" tab.

---

## Pro Tips

### Speed Up Training
- Use pretrained weights
- Reduce image size
- Enable GPU T4x2 (premium)

### Improve Accuracy
- Add more data augmentation
- Train longer (more epochs)
- Ensemble multiple models

### Share Your Work
- Make notebook public
- Add markdown documentation
- Share dataset on Kaggle

---

## Need Help?

See detailed documentation:
- [DATASETS.md](DATASETS.md) - All datasets
- [DATASET_SETUP_CHECKLIST.md](DATASET_SETUP_CHECKLIST.md) - Setup guide
- [README.md](README.md) - Project overview
- [docs/](docs/) - Technical docs

---

## Summary Commands

```bash
# Download dataset
python download_datasets.py

# Verify download
ls data/DeepParticle/MICRO/

# Prepare for Kaggle upload
cd data/DeepParticle
zip -r microplastics-micro.zip MICRO/
```

Then follow Step 2 and 3 above!

---

## Complete Workflow Diagram

```
1. Download Dataset
   ↓
2. Upload to Kaggle
   ↓
3. Create Notebook
   ↓
4. Add Dataset
   ↓
5. Update Paths
   ↓
6. Run Training
   ↓
7. Download Results
```

**Time to first results**: ~30 minutes!

---

**You're ready to start!** Begin with Method 1 (U-Net) as it's the easiest to set up and understand.
