# Melusi 2025 — Small-Area Population Estimation

Integrating high-resolution drone imagery and machine learning for small and informal-area population estimation in Melusi (Atteridgeville, Pretoria).

## Project Overview

This project aims to develop a methodological approach for estimating small-area population in Melusi, an informal settlement near Atteridgeville, Pretoria West. Using high-resolution aerial photographs (3cm spatial resolution) captured by a DJI Zenmuse L1 drone sensor, we apply deep learning and machine learning techniques to detect building footprints and estimate population density.

**Partner:** Department of Geography, Geoinformatics and Meteorology (GGM) & Gauteng Research Triangle (GRT) - INSPIRED, University of Pretoria

**Module:** MIT 808 — Big Data Science Capstone Project, University of Pretoria (2026)

## Team

| Name | GitHub |
|------|--------|
| Kampamba Chanda | @MrChanda |
| Lehlogonolo Mbiza | @Phineas0309 |

## Project Structure
```
melusi-2025/
├── data/               ← not tracked (stored on Google Drive)
│   ├── raw/            ← original drone imagery (ECW, GeoTIFF)
│   ├── processed/      ← cleaned/transformed data
│   └── external/       ← outside datasets
├── notebooks/          ← Jupyter/Colab notebooks
├── src/                ← Python scripts and modules
├── reports/
│   └── figures/        ← saved plots and maps
├── references/         ← papers, manuals, data dictionaries
├── requirements.txt
└── README.md
```

## Setup

### Google Colab (recommended)
1. Open the setup notebook in Colab
2. Run the Session Setup cell — it handles package installation, Drive mount, and repo clone
3. Data is stored on a shared Google Drive folder mounted at:
   `/content/drive/MyDrive/MIT/MIT808/melusi-2025-data/raw/`

### Local (optional, for QGIS visualization)
1. Install QGIS LTR + GDAL via [OSGeo4W](https://trac.osgeo.org/osgeo4w/)
2. Download the ECW file from the shared Google Drive for local visualization

## Data

The drone imagery is **not committed to this repo** due to file size and sensitivity. Data is stored on a shared Google Drive folder. Contact a team member for access.

- **ECW**: Compressed RGB orthophoto (3cm resolution)
- **GeoTIFF**: Uncompressed RGB orthophoto (3cm resolution)
- **GCPs**: 4 ground control points surveyed with RTK-GNSS
- **Drone sensor**: DJI Zenmuse L1 ([specs](https://www.dji.com/global/zenmuse-l1/specs))
