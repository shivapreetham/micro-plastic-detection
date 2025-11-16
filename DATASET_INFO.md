# Dataset Configuration - What You Uploaded

## ✅ Your Upload Structure

You uploaded the **`micro-plastic-sem`** folder directly to Kaggle, which contains:

```
micro-plastic-sem/          ← You uploaded this folder
├── image/                  ← Contains 237 SEM images
│   ├── image_001.tif
│   ├── image_002.tif
│   ├── ...
│   └── image_237.tif
└── label/                  ← Contains 237 binary masks
    ├── image_001.tif
    ├── image_002.tif
    ├── ...
    └── image_237.tif
```

## 📍 Path on Your Computer

**Original location**: 
```
C:\Users\SHIVAPREETHAM ROHITH\Desktop\AI\micro-plastic-detection\data\Microplastics_SEM\dataset1\dataset1\micro-plastic-sem
```

## 📍 Path on Kaggle

After uploading, your dataset will be available at:
```
/kaggle/input/[YOUR-DATASET-NAME]/
├── image/    ← 237 images
└── label/    ← 237 masks
```

**Example**: If you named it `microplastics-sem`, the path would be:
```
/kaggle/input/microplastics-sem/image/
/kaggle/input/microplastics-sem/label/
```

## 🤖 How the Notebook Detects It

The notebook automatically searches for any dataset that contains **both** `image/` and `label/` folders at the root level.

**Detection logic**:
1. Lists all datasets in `/kaggle/input/`
2. For each dataset, checks if `image/` and `label/` folders exist
3. If found, automatically configures paths
4. If not found, shows available datasets and instructions

## ✅ What to Expect in the Notebook

When you run Cell 2 (Dataset Setup), you should see:

```
Configuring Microplastics SEM dataset...
============================================================
Available datasets in /kaggle/input/:
  - microplastics-sem
  - [other datasets if you added any]

Searching for image and label folders...
✓ Found dataset at root level: microplastics-sem

============================================================
DATASET CONFIGURATION
============================================================

✓ Dataset path: /kaggle/input/microplastics-sem
✓ Image directory: /kaggle/input/microplastics-sem/image
✓ Mask directory: /kaggle/input/microplastics-sem/label
✓ Directories exist: True

✓ Total images found: 237
✓ Total masks found: 237

Sample images (first 5):
  - image_001.tif
  - image_002.tif
  - image_003.tif
  - image_004.tif
  - image_005.tif

Sample masks (first 5):
  - image_001.tif
  - image_002.tif
  - image_003.tif
  - image_004.tif
  - image_005.tif

✓ Image and mask counts match!

============================================================
MICROPLASTICS SEM DATASET INFO
============================================================
Source: Mendeley Data
Paper: Automatic quantification and classification of microplastics
Imaging: Scanning Electron Microscopy (SEM)
Particle Size: 50 μm – 1 mm
Types: Fragments, Beads, Fibers
License: CC BY 4.0
============================================================

🚀 Dataset configured successfully! Ready to train.
```

## 🔧 If Auto-Detection Fails

If the notebook can't find your dataset, you'll see:

```
⚠️  ERROR: Could not auto-detect Microplastics SEM dataset!
```

**Solution**: Add a new cell right after Cell 2 with:

```python
# Manual path configuration
DATASET_PATH = "/kaggle/input/YOUR-DATASET-NAME"
IMAGE_DIR = f"{DATASET_PATH}/image"
MASK_DIR = f"{DATASET_PATH}/label"

# Verify paths
import os
print(f"Dataset path: {DATASET_PATH}")
print(f"Image dir exists: {os.path.exists(IMAGE_DIR)}")
print(f"Mask dir exists: {os.path.exists(MASK_DIR)}")
```

Replace `YOUR-DATASET-NAME` with whatever you named your dataset on Kaggle.

## 🎯 Quick Checklist

- [ ] Uploaded the `micro-plastic-sem` folder to Kaggle (not nested folders)
- [ ] Named it something memorable (e.g., `microplastics-sem`)
- [ ] Added the dataset to your notebook ("+ Add data" button)
- [ ] The dataset contains `image/` and `label/` folders at root level
- [ ] Run Cell 2 to see auto-detection results

## 📝 Important Notes

1. **Folder structure matters**: The notebook expects `image/` and `label/` folders to be at the root of your uploaded dataset.

2. **File formats supported**: `.tif`, `.tiff`, `.png`, `.jpg`, `.jpeg` (case-insensitive)

3. **Name matching**: Image and mask files should have the same base filename (e.g., `image_001.tif` in both folders)

4. **No manual editing needed**: If your upload structure is correct, the notebook will automatically detect and configure everything.

## ✨ You're All Set!

Once the notebook shows "🚀 Dataset configured successfully!", you can proceed to run all cells and start training.

**Expected output after full run**:
- Training completes in ~20 minutes
- 4 visualization images saved
- Trained model saved
- Final metrics displayed
