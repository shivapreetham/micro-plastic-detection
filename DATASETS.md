**Microplastics Datasets**

- Use these to source images/masks from seawater, marine/beach, and wastewater contexts. Many require manual download or account acceptance. After download, place files under `data/images` and `data/masks` (matching basenames). If a dataset ships without masks, you can either generate masks (e.g., threshold fluorescence/Nile Red channels) or switch to detection workflows.

- FTIR/hyperspectral sources are listed for completeness; our default pipeline expects 2D images. If you rely on FTIR cubes, export 2D projections or precomputed masks.

1) Zenodo — Microplastic (FTIR hyperspectral image)
   - DOI: 10.5281/zenodo.2555732
   - Link: https://zenodo.org/records/2555732
   - Notes: Environmental plankton sample spiked with microplastics; FTIR hyperspectral. Useful for generating labeled 2D projections or training on precomputed masks.

2) Roboflow Universe — “Microplastics” projects (fluorescence/brightfield microscopy)
   - Link: https://universe.roboflow.com/search?q=microplastic
   - Notes: Several public microplastics image datasets with segmentation or detection annotations. Requires free account and API key. Export as COCO/YOLO/Mask PNGs and place into `data/images` + `data/masks`.

3) Figshare/Zenodo — Nile Red microplastics microscopy (various studies)
   - Example search terms: “Nile Red microplastics microscopy dataset”, “microplastics fluorescence segmentation dataset”. Many studies share image sets with supplementary mask data in repositories.

4) Wastewater/Sewage microplastics microscopy datasets
   - Source examples: institutional repositories (e.g., university data portals, Zenodo, Figshare). Search terms: “wastewater microplastics microscopy dataset segmentation”, “sewage microplastics Nile Red images”.

5) Marine/Beach sediment microplastics microscopy
   - Several studies deposit SEM/optical images and sometimes annotations on Zenodo/Figshare/OSF. Search terms: “SEM microplastics dataset”, “beach sediment microplastics microscopy images annotations”.

If you prefer a turnkey dataset with masks today, I recommend:
- Roboflow Universe projects tagged “microplastics” with segmentation labels (export Mask PNGs).

After placing images and masks:
- Images: `data/images/*.png|jpg`
- Masks:  `data/masks/*.png` (binary mask; same basename as image)

Optional helper for direct downloads:
- `python -m src.data.download_zenodo --url <DIRECT_FILE_URL> --out data/raw`

