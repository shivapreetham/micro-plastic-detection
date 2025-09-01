# Microplastics Detection Project

This project implements U-Net-based segmentation for microplastics detection in water samples.

## Project Structure
```
micro-plastic-detection/
├── venv/                           # Virtual environment
├── data/
│   ├── images/                     # Training images
│   ├── masks/                      # Segmentation masks
│   └── raw/                        # Raw/unprocessed data
├── models/                         # Saved model weights
├── notebooks/                      # Additional notebooks
├── src/                           # Source code modules
├── microplastics_segmentation.ipynb # Main notebook
├── requirements.txt               # Python dependencies
├── setup.bat                      # Setup script
└── run.bat                        # Run script

```

## Quick Start

### 1. First Time Setup:
```bash
# Double-click setup.bat or run in command prompt:
setup.bat
```

### 2. Run the Project:
```bash
# Double-click run.bat or run in command prompt:
run.bat
```

### 3. Manual Setup (Alternative):
```bash
# Activate virtual environment
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

## Usage
1. Run `setup.bat` once to install all dependencies
2. Run `run.bat` to start Jupyter Notebook
3. Open `microplastics_segmentation.ipynb`
4. Run all cells to train the model

## Dependencies
- PyTorch (GPU support)
- OpenCV
- Albumentations
- Scikit-learn
- Matplotlib/Seaborn
- Jupyter Notebook

All dependencies will be installed in the isolated virtual environment.