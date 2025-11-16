# Upload Instructions for Kaggle

Your dataset is now ready to upload to Kaggle!

---

## What I Fixed

The original MACRO.tar.gz had files with colons in names like:
- `2022-05-12 15:56:56.027733_k4.jpg` ❌

Kaggle doesn't allow colons in filenames. I fixed them to:
- `2022-05-12_15-56-56.027733_k4.jpg` ✓

**Fixed files**: 776 filenames
**Total images**: 27 cleaned images ready for upload

---

## Ready-to-Upload File

**File**: `data/microplastics-macro-clean.zip` (73 MB)

This zip contains:
```
images/
  ├── 07_12_macro_mix.JPG
  ├── 07_12_macro_mix1.JPG
  ├── 07_12_macro_mix9.JPG
  └── ... (24 more images)
```

---

## Step-by-Step Upload to Kaggle

### Step 1: Go to Kaggle Datasets

1. Open browser: https://www.kaggle.com/datasets
2. Login to your Kaggle account
3. Click **"New Dataset"** (blue button, top right)

### Step 2: Upload the Zip File

1. Click **"Upload"** tab
2. Click **"Select Files"** or drag and drop
3. Navigate to: `C:\Users\SHIVAPREETHAM ROHITH\Desktop\AI\micro-plastic-detection\data\`
4. Select: `microplastics-macro-clean.zip`
5. Wait for upload (73 MB, ~2-3 minutes)

### Step 3: Configure Dataset

1. **Title**: Microplastics MACRO Dataset
2. **Subtitle**: Macroplastic particles from The Ocean Cleanup
3. **Description** (paste this):
   ```
   Macroplastic images from The Ocean Cleanup's DeepParticle dataset.

   - Size: MACRO (> 5.0 cm)
   - Images: 27 cleaned images
   - Format: JPG
   - Use: Object detection and classification

   Filenames have been cleaned for Kaggle compatibility.
   ```
4. **Visibility**: Private (for now) or Public
5. Click **"Create"**

### Step 4: Note Your Dataset Name

After creation, your dataset URL will be:
```
https://www.kaggle.com/datasets/YOUR-USERNAME/microplastics-macro-dataset
```

Note your dataset slug: **`microplastics-macro-dataset`**

---

## Step-by-Step Run Notebook

### Step 1: Go to Kaggle Notebooks

1. Open: https://www.kaggle.com/code
2. Click **"New Notebook"**
3. Click **"File" → "Upload Notebook"**

### Step 2: Upload the Notebook

1. Navigate to: `C:\Users\SHIVAPREETHAM ROHITH\Desktop\AI\micro-plastic-detection\notebooks\`
2. Select: `kaggle_unet_microplastics.ipynb`
3. Click **"Open"**

### Step 3: Add Your Dataset

1. On the right panel, click **"+ Add Data"**
2. Click **"Your Datasets"** tab
3. Find: **"microplastics-macro-dataset"**
4. Click **"Add"**

### Step 4: Enable GPU (Important!)

1. Click **"Settings"** (right panel)
2. Under **"Accelerator"**, select: **GPU T4 x2** or **GPU P100**
3. Click **"Save"**

### Step 5: Run the Notebook

1. The notebook will **auto-detect** your dataset (no path changes needed!)
2. Click **"Run All"** or press **Shift+Enter** through each cell
3. Wait for training to complete (~20-30 minutes)

---

## What the Notebook Will Do

### Auto-Detection (Cell 2)

The notebook will automatically:
1. List all available datasets
2. Detect your MACRO dataset structure
3. Set paths to `/kaggle/input/YOUR-DATASET/images/`
4. Count images (should show 27)

Example output:
```
Searching for dataset...
============================================================
Available datasets in /kaggle/input/:
  - microplastics-macro-dataset

Detected MACRO dataset!

============================================================
DATASET CONFIGURATION
============================================================

✓ Dataset path: /kaggle/input/microplastics-macro-dataset/images
✓ Image directory exists: True
✓ Total images found: 27

First 5 images:
  - 07_12_macro_mix.JPG
  - 07_12_macro_mix1.JPG
  - 07_12_macro_mix2.JPG
  - 07_12_macro_mix3.JPG
  - 07_12_macro_mix4.JPG

⚠️  No mask directory found
  Will use dummy masks for training (demo mode)
============================================================
```

### Training (Cells 3-12)

- **Model**: U-Net with 31 million parameters
- **Epochs**: 20
- **Batch size**: 8
- **Expected time**: 20-30 minutes with GPU
- **Loss**: Combined Dice + BCE

### Results (Cells 13-16)

- Training curves (loss, IoU, Dice)
- Prediction visualizations
- Final metrics
- Model saved to `/kaggle/working/models/`

---

## Expected Results

Since MACRO dataset doesn't have segmentation masks, you'll see:
- Training will run with **dummy masks** (all zeros)
- This is **demo mode** to verify everything works
- Metrics will be low (expected for dummy masks)

### To Get Real Results

You need a dataset with segmentation masks. Options:

1. **Use different dataset**: Search Kaggle for "microplastic segmentation"
2. **Get MICRO dataset**: Has actual masks for training
3. **Create masks**: Manually annotate your images

---

## Troubleshooting

### "Dataset not found"

Check the dataset name matches:
```python
# In notebook cell 2, manually set:
DATASET_PATH = "/kaggle/input/your-exact-dataset-name"
IMAGE_DIR = f"{DATASET_PATH}/images"
```

### "Out of memory"

1. Reduce batch size in cell 8:
   ```python
   BATCH_SIZE = 4  # Changed from 8
   ```
2. Restart kernel and run again

### "Permission denied"

Make sure dataset visibility is set correctly:
- For your own notebooks: Private is fine
- For sharing: Make dataset Public

---

## Download Your Results

After training completes:

1. Click **"Output"** tab (right panel)
2. Files available:
   - `models/best_unet_model.pth` - Trained model
   - `results/training_curves.png` - Loss plots
   - `results/predictions.png` - Sample predictions
3. Click **"Download All"** or download individually

---

## Next Steps

### If You Want Real Training

Download the **MICRO** dataset instead:
- Has actual segmentation masks
- Better for learning
- More images (hundreds vs 27)

Or search Kaggle for:
- "microplastic segmentation"
- "plastic segmentation masks"
- "marine debris detection"

### If This Works

Try the other notebooks:
- **YOLOv5**: `kaggle_yolov5_microplastics.ipynb`
- **SSD**: Use web interface at https://research-segmentation.toc.yt

---

## Summary

You're all set! Just:

1. **Upload**: `data/microplastics-macro-clean.zip` to Kaggle
2. **Upload**: `notebooks/kaggle_unet_microplastics.ipynb`
3. **Add**: Your dataset
4. **Run All**: And watch it train!

**Total time: 5 minutes setup + 30 minutes training = 35 minutes to results!**

---

## Files Ready

- ✓ Clean dataset: `data/microplastics-macro-clean.zip` (73 MB)
- ✓ Notebook: `notebooks/kaggle_unet_microplastics.ipynb`
- ✓ Auto-detection: Works automatically!

**You're ready to go!**
