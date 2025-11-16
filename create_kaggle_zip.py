"""
Create Kaggle-compatible ZIP file with forward slashes
"""

import os
import zipfile
from pathlib import Path

def create_kaggle_zip(source_dir, output_zip):
    """
    Create a zip file with forward slashes (/) for Kaggle compatibility.
    """
    print(f"Creating Kaggle-compatible ZIP file...")
    print(f"Source: {source_dir}")
    print(f"Output: {output_zip}")
    print()

    file_count = 0

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the source directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Get the full file path
                file_path = os.path.join(root, file)

                # Get relative path from source_dir
                rel_path = os.path.relpath(file_path, source_dir)

                # Convert Windows backslashes to forward slashes
                arcname = rel_path.replace('\\', '/')

                # Add file to zip
                zipf.write(file_path, arcname)
                file_count += 1
                print(f"  Added: {arcname}")

    # Get zip file size
    zip_size = os.path.getsize(output_zip) / (1024 * 1024)  # MB

    print()
    print("="*60)
    print("ZIP FILE CREATED SUCCESSFULLY!")
    print("="*60)
    print(f"Files added: {file_count}")
    print(f"Output file: {output_zip}")
    print(f"File size: {zip_size:.2f} MB")
    print()
    print("This ZIP file is now Kaggle-compatible!")
    print("="*60)

if __name__ == "__main__":
    # Source directory with images
    source_dir = "data/MACRO_clean/images"

    # Output zip file
    output_zip = "data/microplastics-macro-kaggle.zip"

    # Remove old zip if exists
    if os.path.exists(output_zip):
        print(f"Removing old zip file: {output_zip}")
        os.remove(output_zip)

    # Create the zip
    create_kaggle_zip(source_dir, output_zip)

    print("\nNext steps:")
    print("1. Upload this file to Kaggle:")
    print(f"   {os.path.abspath(output_zip)}")
    print("2. Upload the notebook:")
    print("   notebooks/kaggle_unet_microplastics.ipynb")
    print("3. Click 'Run All' and train!")
