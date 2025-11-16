# Dataset Download Instructions

The automated download had issues. Here are manual download options:

---

## Issue Detected

The Python script downloaded an incomplete file (111 MB instead of 541 MB). This is common with large files from Figshare.

---

## Solution 1: Manual Download with Browser (RECOMMENDED)

### Step 1: Download with Browser

1. **Open this link in your browser**:
   ```
   https://figshare.com/ndownloader/files/48254164
   ```

2. **Browser will start download** automatically
   - File name: `48254164` or `48254164.zip`
   - Size: Should be **541 MB**
   - Wait for complete download (may take 5-10 minutes)

3. **Verify download size**:
   - Right-click file → Properties
   - Size should be around **541 MB (567,000,000 bytes)**

### Step 2: Move and Rename File

Move the downloaded file to your project:

**Windows**:
```bash
# If downloaded to Downloads folder
move "%USERPROFILE%\Downloads\48254164" "data\DeepParticle\DeepParticle.zip"
```

**Or manually**:
1. Open File Explorer
2. Go to your Downloads folder
3. Find file `48254164` or `48254164.zip`
4. Copy it to: `c:\Users\SHIVAPREETHAM ROHITH\Desktop\AI\micro-plastic-detection\data\DeepParticle\`
5. Rename to: `DeepParticle.zip`

### Step 3: Extract

**Option A: Using Python script**
```bash
python download_datasets.py
```
(It will detect the file and extract it)

**Option B: Manual extraction**
1. Right-click `DeepParticle.zip`
2. Select "Extract All..."
3. Extract to: `data\DeepParticle\`

---

## Solution 2: Download with PowerShell (Alternative)

```powershell
# Create directory
New-Item -ItemType Directory -Force -Path data\DeepParticle

# Download with better handling
$url = "https://figshare.com/ndownloader/files/48254164"
$output = "data\DeepParticle\DeepParticle.zip"

Write-Host "Downloading DeepParticle dataset (541 MB)..."
Write-Host "This may take 5-10 minutes..."

Invoke-WebRequest -Uri $url -OutFile $output -UseBasicParsing

# Check file size
$size = (Get-Item $output).Length / 1MB
Write-Host "Downloaded: $size MB"

if ($size -lt 500) {
    Write-Host "WARNING: Download incomplete. Please try again or use browser."
} else {
    Write-Host "Download complete!"
    Write-Host "Now extract the file manually or run: python download_datasets.py"
}
```

---

## Solution 3: Use wget (If Installed)

```bash
# Install wget (if not installed)
# Download from: https://eternallybored.org/misc/wget/

# Then download
wget https://figshare.com/ndownloader/files/48254164 -O data/DeepParticle/DeepParticle.zip
```

---

## Solution 4: Use curl

```bash
curl -L https://figshare.com/ndownloader/files/48254164 -o data/DeepParticle/DeepParticle.zip
```

---

## Solution 5: Skip Download - Use Kaggle Directly (EASIEST!)

**You don't need to download locally!**

### Steps:

1. **Find existing dataset on Kaggle**:
   - Go to https://www.kaggle.com/datasets
   - Search: "microplastic" or "ocean cleanup"
   - Popular options:
     - `imtkaggleteam/microplastic-dataset-for-computer-vision`
     - Search for "DeepParticle" or "microplastic segmentation"

2. **Or upload smaller test set**:
   - Use the Mendeley SEM dataset (smaller, easier to download)
   - URL: https://data.mendeley.com/datasets/z6459vntbr/2
   - Size: ~50 MB per file
   - 237 images with masks

3. **Run notebook with Kaggle datasets**:
   - Upload notebook to Kaggle
   - Click "+ Add Data"
   - Search and add existing microplastic datasets
   - No local download needed!

---

## Verification After Download

After successful download, verify:

```bash
# Check file exists and size
ls -lh data/DeepParticle/DeepParticle.zip

# File should show around 541 MB (or 516 MiB)
```

Expected output:
```
-rw-r--r-- 1 user 197121 541M Nov 10 07:15 DeepParticle.zip
```

If size is less than 500 MB, the download is incomplete.

---

## After Successful Download

Once you have the complete file:

### Option 1: Extract with Python script
```bash
python download_datasets.py
```

### Option 2: Extract manually
1. Right-click `DeepParticle.zip`
2. Extract All → Select `data\DeepParticle\`
3. You should see folders: `MICRO/`, `MESO/`, `MACRO/`

### Option 3: Extract with command
```bash
# Windows (PowerShell)
Expand-Archive -Path data\DeepParticle\DeepParticle.zip -DestinationPath data\DeepParticle\

# Or with 7-Zip (if installed)
7z x data\DeepParticle\DeepParticle.zip -odata\DeepParticle\
```

---

## Recommended Approach

**For quickest results**:

1. **Skip local download**
2. **Use Kaggle directly**:
   - Upload notebooks to Kaggle
   - Use existing Kaggle datasets
   - Train on Kaggle's free GPUs

**Benefits**:
- No large downloads
- No local storage needed
- Free GPU access
- Faster training

See [QUICK_START.md](QUICK_START.md) for Kaggle-only workflow.

---

## Alternative Datasets (Easier to Download)

If DeepParticle download keeps failing, use these instead:

### 1. Mendeley SEM Dataset (Smaller)
- **URL**: https://data.mendeley.com/datasets/z6459vntbr/2
- **Size**: ~50 MB per file (3 files total)
- **Images**: 237 with segmentation masks
- **Perfect for**: Method 1 (U-Net)

### 2. Kaggle Datasets (No Download)
- Search on Kaggle: "microplastic"
- Add directly to notebook
- No local download required

### 3. GitHub YOLOv5 Repo (Small)
- **URL**: https://github.com/emailic/YOLOv5-Microplasticos
- Clone with: `git clone https://github.com/emailic/YOLOv5-Microplasticos.git`
- Much smaller dataset included

---

## Need Help?

If you continue having issues:

1. **Use Kaggle directly** (recommended)
2. **Try Mendeley dataset** (smaller files)
3. **Use web interface** for Method 3: https://research-segmentation.toc.yt

See [DATASETS.md](DATASETS.md) for all options!

---

## Summary

**Easiest path forward**:

1. Skip local download
2. Go to Kaggle
3. Use existing datasets on Kaggle
4. Run notebooks there

**Or for local**:

1. Download with browser: https://figshare.com/ndownloader/files/48254164
2. Move to `data\DeepParticle\DeepParticle.zip`
3. Extract manually
4. Start training!
