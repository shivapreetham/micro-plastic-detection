# Kaggle Setup Guide - Microplastics SEM Segmentation

This guide will help you run the U-Net microplastics segmentation notebook on Kaggle.

## 📋 Prerequisites

- Kaggle account (free)
- Microplastics SEM Dataset (located at: `C:\Users\SHIVAPREETHAM ROHITH\Desktop\AI\micro-plastic-detection\data\Microplastics_SEM`)

## 🚀 Step-by-Step Instructions

### Step 1: Upload Dataset to Kaggle

1. **Go to Kaggle Datasets**: https://www.kaggle.com/datasets
2. **Click "New Dataset"** button (top right)
3. **Upload the micro-plastic-sem folder**:
   - Click "Upload Files" or "Select Files from Computer"
   - Navigate to: `C:\Users\SHIVAPREETHAM ROHITH\Desktop\AI\micro-plastic-detection\data\Microplastics_SEM\dataset1\dataset1\micro-plastic-sem`
   - Select the **`micro-plastic-sem`** folder (contains `image/` and `label/` folders directly)
   - **Important**: Upload the folder that directly contains `image/` and `label/` subdirectories

4. **Fill in dataset details**:
   - **Title**: `Microplastics SEM` (or any name you prefer)
   - **Subtitle**: `SEM images of microplastics with segmentation masks`
   - **Description**: 
     ```
     Microplastics Scanning Electron Microscopy (SEM) Dataset
     
     Source: Mendeley Data
     Paper: Automatic quantification and classification of microplastics in scanning electron micrographs
     
     Dataset Contents:
     - 237 high-resolution SEM micrographs
     - Binary segmentation masks for each image
     - Particle size: 50 μm – 1 mm
     - Particle types: Fragments, Beads, Fibers
     
     Structure:
     ├── image/  (237 SEM images)
     └── label/  (237 binary masks)
     
     License: CC BY 4.0
     ```
   - **Tags**: `microplastics`, `segmentation`, `sem`, `microscopy`, `environment`, `pytorch`
   - **License**: CC BY 4.0

5. **Click "Create"** and wait for upload to complete

**Note**: The notebook expects the dataset to have `image/` and `label/` folders at the root level. It will auto-detect this structure.

### Step 2: Create Kaggle Notebook

1. **Go to Kaggle Notebooks**: https://www.kaggle.com/code
2. **Click "New Notebook"** button
3. **Settings**:
   - Click on the three dots (⋮) on the right
   - Select "Notebook options"
   - **Accelerator**: Select **GPU** (P100 or T4 recommended)
   - **Language**: Python
   - **Environment**: Latest available

### Step 3: Add Dataset to Notebook

1. **In your new notebook**, click **"+ Add data"** (right panel)
2. **Search** for your uploaded dataset name (`microplastics-sem-dataset` or whatever you named it)
3. **Click "Add"** next to your dataset
4. The dataset will now be available at `/kaggle/input/[your-dataset-name]/`

### Step 4: Upload Notebook Code

1. **Open the notebook file locally**:
   - Path: `C:\Users\SHIVAPREETHAM ROHITH\Desktop\AI\micro-plastic-detection\notebooks\kaggle_unet_microplastics.ipynb`

2. **In Kaggle notebook**:
   - Click **"File"** → **"Import Notebook"**
   - Upload the `kaggle_unet_microplastics.ipynb` file
   - OR copy-paste each cell manually

### Step 5: Run the Notebook

1. **Verify GPU is enabled**:
   - Check the output of the first cell shows: `Using device: cuda`

2. **Run all cells** (Click "Run All" or run each cell individually with Shift+Enter)

3. **Monitor training**:
   - Watch the progress bars
   - Check loss and metrics after each epoch
   - Training should take ~15-30 minutes on GPU

### Step 6: Download Results

After training completes:

1. **Navigate to Output section** (bottom right panel)
2. **Download**:
   - `best_unet_model.pth` - Trained model weights
   - `training_curves.png` - Loss and metric plots
   - `predictions.png` - Sample predictions
   - `sample_data.png` - Input data samples
   - `final_results.txt` - Summary of results

## 📊 Expected Results

### Training Metrics:
- **Training time**: ~15-30 minutes (20 epochs on GPU)
- **Model size**: ~31 million parameters
- **Expected performance**:
  - IoU: 0.65-0.85
  - Dice: 0.70-0.90
  - F1 Score: 0.70-0.90

### Dataset Split:
- Training: 165 images (70%)
- Validation: 47 images (20%)
- Test: 25 images (10%)

## 🔧 Troubleshooting

### Issue: "Could not auto-detect dataset"

**Solution**: The notebook looks for folders named `image/` and `label/`. Add a new cell after Cell 2:
```python
# Manual configuration if auto-detection fails
DATASET_PATH = "/kaggle/input/YOUR-DATASET-NAME"  # Replace with your dataset name
IMAGE_DIR = f"{DATASET_PATH}/image"
MASK_DIR = f"{DATASET_PATH}/label"

print(f"Manually set paths:")
print(f"  IMAGE_DIR: {IMAGE_DIR}")
print(f"  MASK_DIR: {MASK_DIR}")
print(f"  Image dir exists: {os.path.exists(IMAGE_DIR)}")
print(f"  Mask dir exists: {os.path.exists(MASK_DIR)}")
```

### Issue: "No GPU available"

**Solution**: 
1. Go to notebook settings (⋮ menu)
2. Select "Accelerator" → "GPU"
3. Save and restart session

### Issue: "Out of memory error"

**Solution**: Reduce batch size in Cell 4:
```python
BATCH_SIZE = 4  # Instead of 8
```

### Issue: "Images not loading"

**Solution**: Check your dataset structure:
```python
# Run this in a cell to debug:
import os
for root, dirs, files in os.walk('/kaggle/input/'):
    print(root)
    print('  Dirs:', dirs[:5])
    print('  Files:', files[:5])
```

## 📱 For Your Presentation

### Key Visualizations to Show:
1. **Sample SEM images with masks** (`sample_data.png`)
2. **Training curves** (`training_curves.png`) - show loss decreasing, IoU/Dice increasing
3. **Model predictions** (`predictions.png`) - compare ground truth vs predictions
4. **Final metrics table** - IoU, Dice, F1, Precision, Recall

### Key Points to Mention:
- ✓ Using state-of-the-art U-Net architecture for medical/scientific image segmentation
- ✓ High-resolution SEM imaging provides detailed microplastic structure
- ✓ Binary segmentation: microplastic particles vs. background
- ✓ 237 annotated images with pixel-level masks
- ✓ Automatic detection can help researchers quantify microplastic pollution
- ✓ Can classify particle types: fragments, beads, fibers

### Potential Extensions (Future Work):
- Multi-class segmentation (classify particle types)
- Instance segmentation (separate individual particles)
- Apply to other environmental samples (soil, blood, food)
- Real-time detection system
- Integration with microscopy equipment

## 📚 Dataset Information

**Source**: Mendeley Data  
**DOI**: https://data.mendeley.com/datasets/z6459vntbr/2  
**Paper**: "Automatic quantification and classification of microplastics in scanning electron micrographs"  
**License**: CC BY 4.0  

**Citation**:
```
Schymanski, D., Goldbeck, C., Humpf, H. U., & Fürst, P. (2018). 
Automatic quantification and classification of microplastics in scanning electron micrographs.
```

## 💡 Tips for Kaggle

1. **Save your work frequently** - Kaggle auto-saves, but click "Save Version" to create checkpoints
2. **Enable GPU** - Much faster training (5-10x speedup)
3. **Make notebook public** - Share with professors/peers for your presentation
4. **Add markdown cells** - Document your findings and observations
5. **Experiment** - Try different hyperparameters, save versions to compare

## 🆘 Need Help?

If you encounter issues:
1. Check the auto-detection output in Cell 2
2. Verify dataset structure matches expected format
3. Ensure GPU is enabled in notebook settings
4. Check Kaggle discussion forums
5. Review error messages carefully

## ✅ Checklist Before Presentation

- [ ] Dataset uploaded to Kaggle
- [ ] Notebook runs successfully end-to-end
- [ ] Training curves saved
- [ ] Sample predictions generated
- [ ] Final metrics recorded
- [ ] Model weights downloaded
- [ ] Screenshots/visualizations prepared
- [ ] Results summary ready

Good luck with your presentation! 🎉

---

**Quick Start Command List**:
```bash
# On Kaggle (after setup):
1. Add data → Search "microplastics-sem-dataset" → Add
2. Settings → Accelerator → GPU → Save
3. Run All
4. Wait ~20 minutes
5. Download results from Output section
```
