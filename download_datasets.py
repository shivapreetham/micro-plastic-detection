"""
Dataset Download Script for Microplastics Detection Project

This script downloads the recommended datasets for all 3 methods.
"""

import os
import urllib.request
import zipfile
from pathlib import Path

def download_file(url, destination):
    """Download a file with progress tracking."""
    print(f"Downloading from: {url}")
    print(f"Saving to: {destination}")

    def reporthook(count, block_size, total_size):
        if total_size > 0:
            percent = int(count * block_size * 100 / total_size)
            downloaded_mb = count * block_size / (1024 * 1024)
            total_mb = total_size / (1024 * 1024)
            print(f"\rProgress: {percent}% ({downloaded_mb:.1f}/{total_mb:.1f} MB)", end='', flush=True)
        else:
            downloaded_mb = count * block_size / (1024 * 1024)
            print(f"\rDownloaded: {downloaded_mb:.1f} MB", end='', flush=True)

    try:
        urllib.request.urlretrieve(url, destination, reporthook=reporthook)
        print("\nDownload complete!")
        return True
    except Exception as e:
        print(f"\nDownload failed: {e}")
        return False

def extract_zip(zip_path, extract_to):
    """Extract a zip file."""
    print(f"Extracting {zip_path}...")

    # Verify it's a valid zip file first
    if not zipfile.is_zipfile(zip_path):
        raise Exception(f"Error: {zip_path} is not a valid zip file. The download may have failed or been incomplete.")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted to {extract_to}")

def download_deepparticle():
    """Download DeepParticle dataset (Ocean Cleanup)."""
    print("\n" + "="*60)
    print("DOWNLOADING DEEPPARTICLE DATASET")
    print("="*60)
    print("Source: The Ocean Cleanup + Frontiers Environmental Science 2024")
    print("Size: 541 MB")
    print("Particles: 4,795 annotated microplastics")
    print("="*60 + "\n")

    # Create data directory
    data_dir = Path("data/DeepParticle")
    data_dir.mkdir(parents=True, exist_ok=True)

    # Download URL
    url = "https://figshare.com/ndownloader/files/48254164"
    zip_path = data_dir / "DeepParticle.zip"

    # Check if already extracted
    extracted_folder = data_dir / "MICRO"
    if extracted_folder.exists():
        print(f"Dataset already extracted at: {data_dir}")
        print("Skipping download and extraction.")
        return

    # Download
    if not zip_path.exists():
        print("Starting download...")
        success = download_file(url, str(zip_path))
        if not success:
            print("\nDownload failed. Please try manual download:")
            print("1. Visit: https://figshare.com/ndownloader/files/48254164")
            print("2. Save as: data/DeepParticle/DeepParticle.zip")
            print("3. Run this script again")
            return
    else:
        print(f"File already exists: {zip_path}")
        print("Verifying file...")

    # Verify file size (should be around 541 MB)
    file_size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"Downloaded file size: {file_size_mb:.1f} MB")

    if file_size_mb < 500:
        print("\nWARNING: File size is too small. Download may be incomplete.")
        print("Deleting incomplete file...")
        zip_path.unlink()
        print("Please run the script again to retry download.")
        return

    # Extract
    try:
        print("\nExtracting dataset...")
        extract_zip(str(zip_path), str(data_dir))
    except Exception as e:
        print(f"\nExtraction failed: {e}")
        print("\nTroubleshooting:")
        print("1. Delete the file: data/DeepParticle/DeepParticle.zip")
        print("2. Run this script again to re-download")
        print("\nOr download manually from:")
        print("https://figshare.com/ndownloader/files/48254164")
        return

    print("\n" + "="*60)
    print("DEEPPARTICLE DATASET READY!")
    print("="*60)
    print(f"Location: {data_dir}")
    print("\nDataset structure:")
    print("  - MICRO/raw_img/  (microplastics 0.05-0.5 cm)")
    print("  - MESO/raw_img/   (mesoplastics 0.5-5.0 cm)")
    print("  - MACRO/raw_img/  (macroplastics > 5.0 cm)")
    print("\nParticle types: hard, pellet, line, foam, noise")
    print("="*60 + "\n")

def main():
    """Main function to download all datasets."""
    print("\n" + "="*60)
    print("MICROPLASTICS DATASET DOWNLOADER")
    print("="*60)
    print("\nThis script will download the following datasets:")
    print("1. DeepParticle Dataset (Ocean Cleanup) - 541 MB")
    print("   - Best for all 3 methods")
    print("   - Marine/ocean microplastics")
    print("   - 4,795 annotated particles")
    print("\n" + "="*60 + "\n")

    # Ask user confirmation
    response = input("Do you want to download DeepParticle dataset? (yes/no): ").lower()

    if response in ['yes', 'y']:
        download_deepparticle()
    else:
        print("\nDownload cancelled.")
        print("\nTo download manually:")
        print("1. Visit: https://figshare.com/ndownloader/files/48254164")
        print("2. Save as: data/DeepParticle/DeepParticle.zip")
        print("3. Extract the zip file")

    print("\n" + "="*60)
    print("ADDITIONAL DATASETS")
    print("="*60)
    print("\nOther recommended datasets (manual download):")
    print("\n1. Microplastics SEM Dataset (Mendeley):")
    print("   URL: https://data.mendeley.com/datasets/z6459vntbr/2")
    print("   Size: ~500 MB")
    print("   Images: 237 SEM micrographs")
    print("   Best for: Method 1 (U-Net) with segmentation masks")

    print("\n2. YOLOv5 Microplastics (GitHub):")
    print("   URL: https://github.com/emailic/YOLOv5-Microplasticos")
    print("   Command: git clone https://github.com/emailic/YOLOv5-Microplasticos.git")
    print("   Best for: Method 2 (YOLOv5) pre-configured")

    print("\n3. Kaggle Datasets:")
    print("   - Microplastic Dataset for Computer Vision")
    print("   - URL: https://www.kaggle.com/datasets/imtkaggleteam/microplastic-dataset-for-computer-vision")
    print("   - Add directly in Kaggle notebooks")

    print("\nSee DATASETS.md for complete information!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
