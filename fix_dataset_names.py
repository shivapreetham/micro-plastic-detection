"""
Fix Dataset Filenames for Kaggle Upload

This script fixes invalid characters in filenames (colons, etc.) that Kaggle doesn't allow.
"""

import os
import shutil
import tarfile
from pathlib import Path

def extract_and_fix_names(tar_path, output_dir):
    """
    Extract tar.gz and fix filenames by removing invalid characters.
    Fixed to handle Windows filename restrictions.
    """
    print(f"Extracting {tar_path}...")

    os.makedirs(output_dir, exist_ok=True)

    # Extract tar.gz with filename fixing
    renamed_count = 0
    with tarfile.open(tar_path, 'r:gz') as tar:
        for member in tar.getmembers():
            # Get the original name
            original_name = member.name

            # Fix the name by removing invalid characters
            fixed_name = original_name
            if ':' in fixed_name or ' ' in fixed_name:
                fixed_name = fixed_name.replace(':', '-').replace(' ', '_')
                renamed_count += 1
                if renamed_count <= 10:  # Only print first 10
                    print(f"  Fixing: {os.path.basename(original_name)} -> {os.path.basename(fixed_name)}")

            # Update member name
            member.name = fixed_name

            # Extract with fixed name
            try:
                tar.extract(member, output_dir)
            except Exception as e:
                print(f"  Warning: Could not extract {fixed_name}: {e}")

    print(f"Extracted to {output_dir}")
    print(f"Total files renamed during extraction: {renamed_count}")
    return output_dir

def create_clean_dataset(input_dir, output_dir):
    """
    Create a clean version of the dataset with only images (no subcategories).
    """
    print(f"\nCreating clean dataset...")

    # Create output directories
    images_dir = os.path.join(output_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    # Copy all images from raw_img
    raw_img_dir = os.path.join(input_dir, 'MACRO', 'raw_img')

    if os.path.exists(raw_img_dir):
        image_count = 0
        for file in os.listdir(raw_img_dir):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')):
                src = os.path.join(raw_img_dir, file)
                dst = os.path.join(images_dir, file)
                shutil.copy2(src, dst)
                image_count += 1

        print(f"Copied {image_count} images to {images_dir}")
    else:
        print(f"ERROR: {raw_img_dir} not found!")

    return output_dir

def main():
    """Main function."""
    print("="*60)
    print("DATASET FILENAME FIXER")
    print("="*60)

    # Paths
    tar_path = "data/MACRO.tar.gz"
    extract_dir = "data/MACRO_extracted"
    clean_dir = "data/MACRO_clean"

    if not os.path.exists(tar_path):
        print(f"\nERROR: {tar_path} not found!")
        print("Please ensure MACRO.tar.gz is in the data/ directory.")
        return

    print(f"\nStep 1: Extracting and fixing filenames...")
    extract_and_fix_names(tar_path, extract_dir)

    print(f"\nStep 2: Creating clean dataset for Kaggle upload...")
    create_clean_dataset(extract_dir, clean_dir)

    print("\n" + "="*60)
    print("DONE!")
    print("="*60)
    print(f"\nClean dataset ready for Kaggle upload:")
    print(f"  Location: {clean_dir}/images/")
    print(f"\nNext steps:")
    print("  1. Zip the folder:")
    print(f"     zip -r MACRO_clean.zip {clean_dir}/images/")
    print("  2. Upload MACRO_clean.zip to Kaggle")
    print("  3. Run the notebook!")
    print("="*60)

if __name__ == "__main__":
    main()
