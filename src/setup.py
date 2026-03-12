"""
Melusi 2025 — Shared Environment Setup
=======================================
Importable module that configures paths, validates packages,
sets plotting defaults, and provides common imports.

Usage (from any notebook, after the bootstrap cell):
    from src.setup import configure_environment, PATHS
    configure_environment()
"""

import importlib
import sys
import os
import warnings

# ──────────────────────────────────────────────
# 1. PATH CONSTANTS
# ──────────────────────────────────────────────
# Central place for every path used in the project.
# If a folder moves, you change it here — once.

PATHS = {
    "data_raw":    "/content/drive/MyDrive/MIT/MIT808/melusi-2025-data/raw/",
    "repo":        "/content/melusi-2025",
    "notebooks":   "/content/melusi-2025/notebooks",
    "src":         "/content/melusi-2025/src",
    "figures":     "/content/melusi-2025/reports/figures",
}


# ──────────────────────────────────────────────
# 2. REQUIRED PACKAGES
# ──────────────────────────────────────────────
# Maps import name → pip name (they differ for some packages).
# Used by check_packages() to verify everything is installed.

REQUIRED_PACKAGES = {
    "numpy":      "numpy",
    "pandas":     "pandas",
    "matplotlib": "matplotlib",
    "seaborn":    "seaborn",
    "rasterio":   "rasterio",
    "geopandas":  "geopandas",
    "earthpy":    "earthpy",
    "contextily": "contextily",
    "osgeo":      "GDAL",        # GDAL imports as osgeo
    "laspy":      "laspy",
}


def check_packages(required: dict = None) -> None:
    """
    Verify that all required packages are importable.
    Prints a status line for each and raises an error
    if any are missing — so you catch it immediately
    rather than halfway through an analysis.

    Parameters
    ----------
    required : dict, optional
        {import_name: pip_name} mapping.
        Defaults to REQUIRED_PACKAGES.
    """
    if required is None:
        required = REQUIRED_PACKAGES

    missing = []
    for import_name, pip_name in required.items():
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing.append(pip_name)

    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print(f"   Run: pip install -q {' '.join(missing)}")
        raise ImportError(f"Install missing packages before continuing.")
    else:
        print(f"✅ All {len(required)} required packages available")


def configure_plots() -> None:
    """
    Set matplotlib and seaborn defaults for clean,
    publication-quality figures that look good in both
    the notebook and the KDD report.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.rcParams.update({
        "figure.figsize":       (12, 8),
        "figure.dpi":           100,
        "savefig.dpi":          150,
        "font.size":            11,
        "axes.titlesize":       13,
        "axes.labelsize":       11,
    })
    sns.set_style("whitegrid")
    print("✅ Plot defaults configured")


def ensure_dirs() -> None:
    """
    Create output directories if they don't exist yet.
    Particularly the figures directory — we'll save
    every EDA plot there for the report.
    """
    for key in ["figures"]:
        path = PATHS[key]
        os.makedirs(path, exist_ok=True)
    print(f"✅ Output directories verified")


def configure_environment() -> None:
    """
    One-call setup: validates packages, sets plot defaults,
    creates directories, and suppresses noisy warnings.

    Call this once at the top of every notebook after
    the bootstrap cell.
    """
    # Suppress common geospatial warnings that clutter output
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", message=".*PyGEOS.*")

    check_packages()
    configure_plots()
    ensure_dirs()

    print("─" * 40)
    print("🚀 Environment ready")
    print(f"   Data:    {PATHS['data_raw']}")
    print(f"   Repo:    {PATHS['repo']}")
    print(f"   Figures: {PATHS['figures']}")
