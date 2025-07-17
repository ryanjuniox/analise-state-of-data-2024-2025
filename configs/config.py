"""
Configurações gerais do projeto
"""

import os
from pathlib import Path

# Caminhos do projeto
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Configurações de visualização
FIGURE_DPI = 300
FIGURE_FORMAT = "png"
SEABORN_STYLE = "whitegrid"
COLOR_PALETTE = "viridis"

# Configurações gerais
RANDOM_STATE = 42
