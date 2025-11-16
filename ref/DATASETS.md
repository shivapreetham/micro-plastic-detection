# Microplastics Datasets - Complete Guide

This document lists all recommended datasets for microplastic detection, segmentation, and classification from seawater, beach, marine, and sewage sources.

---

## Dataset 1: DeepParticle Dataset (RECOMMENDED - Ocean Cleanup)

### Overview
- **Source**: The Ocean Cleanup + Frontiers Environmental Science 2024
- **Paper**: [Computer vision segmentation model—deep learning for categorizing microplastic debris](https://www.frontiersin.org/journals/environmental-science/articles/10.3389/fenvs.2024.1386292/full)
- **Total Particles**: 4,795 annotated microplastic particles
- **Environment**: Marine/Ocean cleanup operations
- **License**: Apache 2.0

### Size Categories
1. **MICRO**: 0.05 cm – 0.5 cm (microplastics)
2. **MESO**: 0.5 cm – 5.0 cm (mesoplastics)
3. **MACRO**: > 5.0 cm (macroplastics)

### Particle Types
- **Hard fragments**: Rigid plastic pieces
- **Pellets**: Pre-production plastic pellets (nurdles)
- **Lines/Fibers**: Thread-like plastic materials
- **Foam**: Expanded polystyrene and similar materials
- **Caps**: Bottle caps (MESO/MACRO)
- **Butts**: Cigarette butts (MESO)
- **Noise**: Background/non-plastic items (for false positive reduction)

### Download Links

#### Direct Download (Figshare)
```
https://figshare.com/ndownloader/files/48254164
```
**File**: `26511253.zip` (541 MB)

#### Alternative: GitLab Repository
```
https://gitlab.com/Grouumf/particle_detect
```

### Dataset Structure
```
DeepParticle/
├── MICRO/
│   ├── raw_img/          # Original images
│   ├── annotation/       # Bounding box annotations
│   ├── line/            # Fiber particles
│   ├── pellet/          # Pellet particles
│   ├── foam/            # Foam particles
│   └── noise/           # Non-plastic items
├── MESO/
│   ├── raw_img/
│   ├── annotation/
│   ├── hard/
│   ├── pellet/
│   ├── line/
│   ├── cap_me/
│   └── butt_me/
└── MACRO/
    ├── raw_img/
    ├── annotation/
    └── [particle types]
```

### Use Cases
- **Method 1 (U-Net)**: Use raw images for segmentation
- **Method 2 (YOLOv5)**: Use annotations for object detection
- **Method 3 (SSD)**: Use for classification tasks

### Quick Download Command
```bash
cd data/
wget https://figshare.com/ndownloader/files/48254164 -O DeepParticle.zip
unzip DeepParticle.zip
```

---

## Dataset 2: Microplastics SEM Dataset (Mendeley)

### Overview
- **Source**: Mendeley Data
- **Paper**: Automatic quantification and classification of microplastics in scanning electron micrographs
- **Images**: 237 SEM micrographs
- **Particle Size**: 50 μm – 1 mm
- **Imaging**: Scanning Electron Microscopy (SEM)
- **License**: CC BY 4.0

### Download Link
```
https://data.mendeley.com/datasets/z6459vntbr/2
```

### Contents
- **dataset1.zip**: Training data for semantic segmentation + shape classification
- **dataset2.zip**: Instance segmentation datasets
- **dataset3.zip**: Original SEM micrographs with ground-truth labels

### Dataset Structure
```
Microplastics_SEM/
├── dataset1/
│   └── [datasets_full]_Exp1_Exp4/
│       ├── image/    # 237 SEM images
│       └── label/    # Binary segmentation masks
├── dataset2/
│   └── [instance segmentation data]
└── dataset3/
    └── [original SEM images]
```

### Particle Types
- Fragments
- Beads
- Fibers (diameter ~10 μm)

### Use Cases
- **Method 1 (U-Net)**: PERFECT - Has segmentation masks
- High-resolution SEM imaging
- Academic research

### Quick Download
Visit Mendeley link above, download all 3 zip files manually.

---

## Dataset 3: Microplastic Dataset for Computer Vision (Kaggle)

### Overview
- **Source**: Kaggle
- **Link**: https://www.kaggle.com/datasets/imtkaggleteam/microplastic-dataset-for-computer-vision
- **Format**: Ready for object detection
- **Environment**: Mixed sources

### Use Cases
- **Method 2 (YOLOv5)**: Pre-formatted for YOLO
- Object detection tasks
- Quick Kaggle integration

### How to Use
1. Go to Kaggle notebook
2. Add dataset via "+ Add Data"
3. Search: "microplastic-dataset-for-computer-vision"
4. Run notebook

---

## Dataset 4: YOLOv5 Microplastics (GitHub)

### Overview
- **Source**: GitHub - emailic/YOLOv5-Microplasticos
- **Link**: https://github.com/emailic/YOLOv5-Microplasticos
- **Format**: YOLO format with bounding boxes
- **Ready to use**: Pre-configured for YOLOv5

### Download
```bash
git clone https://github.com/emailic/YOLOv5-Microplasticos.git
cd YOLOv5-Microplasticos
```

### Use Cases
- **Method 2 (YOLOv5)**: Ready-made repository
- Pre-trained models available
- Training scripts included

---

## Dataset 5: Sewage Microplastics (Preprints.org)

### Overview
- **Source**: Microscopic Image Dataset with Segmentation and Detection Labels for Microplastic Analysis in Sewage
- **Paper**: https://www.preprints.org/manuscript/202404.1478/v1
- **Environment**: Wastewater treatment plants / Sewage
- **Labels**: Both segmentation and detection labels

### Contents
- Microscopic images from sewage samples
- Segmentation masks
- Bounding box annotations
- GitHub repository with code

### Use Cases
- Sewage-specific applications
- Wastewater monitoring
- Both segmentation and detection

---

## Dataset 6: NOAA Marine Microplastics Database

### Overview
- **Source**: NOAA NCEI (National Centers for Environmental Information)
- **Link**: https://www.ncei.noaa.gov/products/microplastics
- **Scope**: Global marine microplastics data
- **Samples**: 8,218+ pelagic microplastic samples
- **Coverage**: World's oceans + Laurentian Great Lakes

### Access
- GIS web map portal
- Downloadable CSV data
- Global spatial distribution
- Temporal trends

### Use Cases
- Research and analysis
- Geographic distribution studies
- Temporal trend analysis

---

## Dataset 7: Marine Microplastics Kaggle Datasets

### Dataset 7a: NOAA Marine Microplastic Density
- **Link**: https://www.kaggle.com/datasets/brsdincer/marine-microplastic-on-world-density-noaa
- **Format**: CSV with lat/lon coordinates
- **Source**: NOAA data

### Dataset 7b: Microplastics in the Oceans
- **Link**: https://www.kaggle.com/datasets/mselimozen/microplastics-in-the-oceans
- **Samples**: 8,218 observations
- **Format**: Structured data

---

## Recommended Dataset Combinations

### For Quick Start (Best for Beginners)
1. **DeepParticle Dataset** (541 MB) - All 3 methods
   - Download: `wget https://figshare.com/ndownloader/files/48254164`

### For Academic Research
1. **Microplastics SEM** (Mendeley) - Method 1 (U-Net)
2. **DeepParticle** - Methods 2 & 3

### For Sewage-Specific Work
1. **Sewage Microplastics** (Preprints.org)
2. **DeepParticle** (for comparison)

### For Marine/Ocean Focus
1. **DeepParticle** (Ocean Cleanup data)
2. **NOAA Database** (spatial analysis)

---

## Dataset Comparison Table

| Dataset | Size | Images | Environment | Segmentation | Detection | Classification | Best For |
|---------|------|--------|-------------|--------------|-----------|----------------|----------|
| **DeepParticle** | 541 MB | 4,795+ | Marine/Ocean | ✓ | ✓ | ✓ | All methods |
| **SEM Mendeley** | ~500 MB | 237 | Lab (SEM) | ✓ | ✗ | ✓ | U-Net |
| **Kaggle CV** | Varies | Varies | Mixed | ✗ | ✓ | ✗ | YOLOv5 |
| **YOLOv5 GitHub** | Small | ~100 | Mixed | ✗ | ✓ | ✗ | YOLOv5 |
| **Sewage** | Medium | Varies | Sewage | ✓ | ✓ | ✗ | Wastewater |
| **NOAA** | Large | 8,218+ | Ocean/Lakes | ✗ | ✗ | ✗ | Analysis |

---

## Quick Start Commands

### Download DeepParticle Dataset
```bash
# Create data directory
mkdir -p data/DeepParticle
cd data/DeepParticle

# Download dataset
wget https://figshare.com/ndownloader/files/48254164 -O DeepParticle.zip

# Extract
unzip DeepParticle.zip

# Verify
ls -lh
```

### Download Mendeley SEM Dataset
1. Visit: https://data.mendeley.com/datasets/z6459vntbr/2
2. Click "Download All" (requires free Mendeley account)
3. Extract to `data/Microplastics_SEM/`

### Clone YOLOv5 Repository
```bash
cd methods/
git clone https://github.com/emailic/YOLOv5-Microplasticos.git
```

---

## Dataset Setup for Each Method

### Method 1: U-Net Segmentation
**Best Dataset**: DeepParticle OR Microplastics SEM

```bash
# Option A: DeepParticle
IMAGE_DIR = "data/DeepParticle/MICRO/raw_img"
MASK_DIR = "data/DeepParticle/MICRO/annotation"  # Convert to masks

# Option B: Mendeley SEM
IMAGE_DIR = "data/Microplastics_SEM/dataset1/[datasets_full]_Exp1_Exp4/image"
MASK_DIR = "data/Microplastics_SEM/dataset1/[datasets_full]_Exp1_Exp4/label"
```

### Method 2: YOLOv5 Detection
**Best Dataset**: DeepParticle OR YOLOv5-Microplasticos

```bash
# Option A: DeepParticle (has annotations)
DATASET_DIR = "data/DeepParticle/MICRO"

# Option B: Pre-made YOLOv5 repo
cd YOLOv5-Microplasticos
# Follow their README
```

### Method 3: SSD Classification
**Best Dataset**: DeepParticle

```bash
IMAGE_DIR = "data/DeepParticle/MICRO/raw_img"
# Includes reference coin for size calibration
```

---

## Upload to Kaggle

### For DeepParticle Dataset

1. **Prepare folder structure**:
```bash
# For U-Net
mkdir kaggle_upload_unet
cp -r data/DeepParticle/MICRO/raw_img kaggle_upload_unet/image
cp -r data/DeepParticle/MICRO/annotation kaggle_upload_unet/label
zip -r microplastics-deepparticle-unet.zip kaggle_upload_unet/

# For YOLOv5
zip -r microplastics-deepparticle-yolo.zip data/DeepParticle/MICRO/
```

2. **Upload to Kaggle**:
   - Go to https://www.kaggle.com/datasets
   - Click "New Dataset"
   - Upload zip file
   - Name: `microplastics-deepparticle`

---

## Citation Information

### DeepParticle Dataset
```
Royer, S.-J., Wolter, H., Delorme, A., Lebreton, L., & Poirion, O. (2024).
Computer vision segmentation model—deep learning for categorizing microplastic debris.
Frontiers in Environmental Science, 12, 1386292.
https://doi.org/10.3389/fenvs.2024.1386292
```

### Microplastics SEM Dataset
```
Automatic quantification and classification of microplastics in scanning
electron micrographs via deep learning. Science of The Total Environment.
https://data.mendeley.com/datasets/z6459vntbr/2
```

---

## Support & Resources

- **DeepParticle GitLab**: https://gitlab.com/Grouumf/particle_detect
- **Docker Image**: `docker.io/opoirion/particle_detect`
- **Web Interface**: https://research-segmentation.toc.yt
- **NOAA Portal**: https://www.ncei.noaa.gov/products/microplastics

---

## Next Steps

1. **Download DeepParticle dataset** (recommended starting point)
2. **Extract and organize** into `data/` folder
3. **Upload to Kaggle** for cloud-based training
4. **Run notebooks** from the `notebooks/` folder

All three notebooks are configured to work with the DeepParticle dataset!
