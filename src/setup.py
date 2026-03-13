"""
Melusi 2025 — Shared Environment Setup
=======================================
Importable module that configures paths, validates packages,
sets plotting defaults, and provides common imports.

Usage (from any notebook, after the bootstrap cell):
    from src.setup import configure_environment, PATHS, save_and_push
    configure_environment()
"""

import importlib
import subprocess
import shutil
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
    "geotiff":     "/content/drive/MyDrive/MIT/MIT808/melusi-2025-data/raw/GeoTIFF/Melusi_07032025Tif.tif",
    "ecw":         "/content/drive/MyDrive/MIT/MIT808/melusi-2025-data/raw/ECW/melusi_RGB_07032025.ecw",
    "repo":        "/content/melusi-2025",
    "notebooks":   "/content/melusi-2025/notebooks",
    "src":         "/content/melusi-2025/src",
    "figures":     "/content/melusi-2025/reports/figures",
    "colab_nb":    "/content/drive/MyDrive/Colab Notebooks",
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
    "osgeo":      "GDAL",
    "laspy":      "laspy",
}


# ──────────────────────────────────────────────
# 3. ENVIRONMENT CONFIGURATION
# ──────────────────────────────────────────────

def check_packages(required: dict = None) -> None:
    """
    Verify that all required packages are importable.
    Prints a status line for each and raises an error
    if any are missing.
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
        raise ImportError("Install missing packages before continuing.")
    else:
        print(f"✅ All {len(required)} required packages available")


def configure_plots() -> None:
    """
    Set matplotlib and seaborn defaults for clean,
    publication-quality figures.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.rcParams.update({
        "figure.figsize":  (12, 8),
        "figure.dpi":      100,
        "savefig.dpi":     150,
        "font.size":       11,
        "axes.titlesize":  13,
        "axes.labelsize":  11,
    })
    sns.set_style("whitegrid")
    print("✅ Plot defaults configured")


def ensure_dirs() -> None:
    """
    Create output directories if they don't exist yet.
    """
    for key in ["figures"]:
        path = PATHS[key]
        os.makedirs(path, exist_ok=True)
    print("✅ Output directories verified")


def configure_environment() -> None:
    """
    One-call setup: validates packages, sets plot defaults,
    creates directories, and suppresses noisy warnings.

    Call this once at the top of every notebook after
    the bootstrap cell.
    """
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


# ──────────────────────────────────────────────
# 4. GIT HELPER
# ──────────────────────────────────────────────

def save_and_push(notebook_name, message="Update notebook"):
    """
    Copy a notebook from Colab's auto-save location into the
    repo, commit it, and push to the current active branch.

    Works for any contributor — it detects which branch you're
    on automatically, so no hardcoded branch names.

    Parameters
    ----------
    notebook_name : str
        Filename of the notebook, e.g. "01_eda.ipynb"
    message : str
        Git commit message describing what changed.

    Usage
    -----
        save_and_push("01_eda.ipynb", "Add Phase 2: metadata inspection")
    """
    repo_dir   = PATHS["repo"]
    drive_path = os.path.join(PATHS["colab_nb"], notebook_name)
    repo_path  = os.path.join(PATHS["notebooks"], notebook_name)

    # --- Check the notebook exists on Drive ---
    if not os.path.exists(drive_path):
        print(f"❌ Notebook not found at: {drive_path}")
        print(f"   Check the filename or save the notebook first.")
        return

    # --- Copy from Drive into repo ---
    shutil.copy(drive_path, repo_path)
    print(f"📋 Copied {notebook_name} into repo")

    # --- Detect current branch ---
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=repo_dir,
        capture_output=True, text=True
    )
    branch = result.stdout.strip()

    # --- Stage, commit, push ---
    subprocess.run(
        ["git", "add", f"notebooks/{notebook_name}"],
        cwd=repo_dir
    )

    commit_result = subprocess.run(
        ["git", "commit", "-m", message],
        cwd=repo_dir,
        capture_output=True, text=True
    )

    if "nothing to commit" in commit_result.stdout:
        print("ℹ️  No changes to commit — notebook is already up to date")
        return

    push_result = subprocess.run(
        ["git", "push", "origin", branch],
        cwd=repo_dir,
        capture_output=True, text=True
    )

    if push_result.returncode == 0:
        print(f"✅ Pushed {notebook_name} to {branch}")
    else:
        print(f"❌ Push failed: {push_result.stderr}")