# Small-Area Population Estimation in Melusi Informal Settlement Using Drone Imagery and Machine Learning
==============================

_This documentation provides information about the Data Insights Drivers MIT 808 capstone project for 2026._

Last updated: March 2026

## Table of contents

1. [Project Description](#project-description)
2. [Project Organization](#project-organization)
3. [Getting Started](#getting-started)
4. [Authors](#authors)
5. [More Information](#more-information)

## Project Description

Accurate, up-to-date population data for informal settlements in South Africa is critically lacking. Official census data is often outdated and coarse-grained, making it difficult for planners and service providers to allocate resources effectively.

This project develops a two-stage machine learning pipeline to estimate small-area population in **Melusi**, an informal settlement near Atteridgeville, City of Tshwane, using high-resolution drone imagery. The pipeline combines:

1. **U-Net Deep Learning Model** — semantic segmentation of a 3cm resolution drone orthophoto to extract individual dwelling footprints
2. **Random Forest Regression Model** — population estimation by linking extracted dwelling footprints to household survey data from GRT-INSPIRED (University of Pretoria)

Primary data inputs include a 7.03 GB GeoTIFF orthophoto (102,730 × 41,815 px, 4-band), a LiDAR point cloud (295.7M points), and an 8,119-record household survey dataset covering Melusi residents. External data sources include Stats SA Census 2022, OpenStreetMap, and Microsoft/Google open building footprints.

The project is conducted in partnership with **Samy Katumba, GGM/GRT-INSPIRED, University of Pretoria**.

## Project Organization

```
├── LICENSE
├── Makefile                        <- Makefile with commands like `make data` or `make train`
├── README.md                       <- The top-level README for developers using this project.
├── data
│   ├── external                    <- Data from third party sources (Census 2022, OSM, open building footprints).
│   ├── interim                     <- Intermediate data that has been transformed (tiled patches, feature arrays).
│   ├── processed                   <- The final, canonical data sets for modeling.
│   └── raw                         <- The original, immutable data dump (orthophoto, LiDAR, household survey).
│
├── docs                            <- Project documentation
│
├── models                          <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks                       <- Jupyter notebooks. Naming convention is a number (for ordering),
│                                      the creator's initials, and a short `-` delimited description, e.g.
│                                      `1.0-kc-initial-data-exploration`.
│
├── references                      <- Data dictionaries, manuals, GCP coordinates, and all other explanatory materials.
│
├── reports                         <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures                     <- Generated graphics and figures to be used in reporting
│
├── requirements.txt                <- The requirements file for reproducing the analysis environment,
│                                      generated with `pip freeze > requirements.txt`
│
├── setup.py                        <- Makes project pip installable (pip install -e .) so src can be imported
├── src                             <- Source code for use in this project.
│   ├── __init__.py                 <- Makes src a Python module
│   │
│   ├── data                        <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features                    <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models                      <- Scripts to train models and then use trained models to make predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization               <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini                         <- tox file with settings for running tox; see tox.testrun.org
```

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## Getting Started

This project runs primarily on **Google Colab** with data stored in **Google Drive**. All notebooks include a bootstrap cell that handles environment setup automatically.

### Prerequisites

- Python 3.10+
- Google Colab (paid compute recommended for large raster processing)
- Google Drive with the `melusi-2025-data` dataset mounted at `/content/drive/MyDrive/MIT/MIT808/melusi-2025-data/`
- A GitHub Personal Access Token stored as a Colab Secret (`gitToken`)

Key libraries:

- `rasterio` — raster data I/O and processing
- `geopandas` — vector/spatial data handling
- `GDAL` — geospatial data abstraction
- `laspy` — LiDAR point cloud processing
- `earthpy` — raster band manipulation
- `torch` / `segmentation-models-pytorch` — U-Net model training
- `scikit-learn` — Random Forest regression

### Installation

Each notebook contains a bootstrap cell that handles setup. To replicate manually:

1. Clone the repository:

```bash
git clone https://github.com/up-mitc-ds/mit808-2026-project-data-insight-drivers.git
cd mit808-2026-project-data-insight-drivers
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make `src` importable:

```bash
pip install -e .
```

### Usage

Notebooks are numbered sequentially and should be run in order:

```
notebooks/01_kc-lm-eda.ipynb          <- Exploratory Data Analysis (orthophoto, LiDAR, survey)
notebooks/02_kc-lm-preprocessing.ipynb <- Tiling, patch generation, feature engineering
notebooks/03_kc-lm-unet-training.ipynb  <- U-Net dwelling segmentation model
notebooks/04_kc-lm-rf-population.ipynb  <- Random Forest population estimation model
```

To run pipeline steps via Makefile (on a local machine):

```bash
make data       # Run data preparation scripts
make features   # Build features from processed data
make train      # Train the U-Net and Random Forest models
make predict    # Generate population estimates
```

## Authors

* **Kampamba Chanda** — [kchanda.kc@gmail.com](mailto:kchanda.kc@gmail.com) | GitHub: [@MrChanda](https://github.com/MrChanda)
* **Lehlogonolo Mbiza** — GitHub: [@Phineas0309](https://github.com/Phineas0309)

### Contributions

| Team Member | Contributions |
|---|---|
| Kampamba Chanda | EDA (orthophoto, LiDAR), project setup, src module, Git workflow, U-Net model development |
| Lehlogonolo Mbiza | EDA (survey data), feature engineering, Random Forest model development |

**External Partner / Supervisor:** Samy Katumba, GGM/GRT-INSPIRED, University of Pretoria

## More Information

- **Study Area:** Melusi Informal Settlement, Atteridgeville, City of Tshwane, Gauteng, South Africa
- **Drone Sensor:** DJI Zenmuse L1 (RGB Mapping Camera, 3cm GSD)
- **Coordinate System:** Lo29 (South Africa Lo coordinate system)
- **Partner Organisation:** GRT-INSPIRED, Department of Geography, Geoinformatics and Meteorology, University of Pretoria
- **Module:** MIT 808 — Capstone Project in Data Science, University of Pretoria, 2026
