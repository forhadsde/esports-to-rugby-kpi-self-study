"""Shared helpers: paths, seeds and saving results."""
import json
import os
import random
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROC = ROOT / "data" / "processed"
FIG = ROOT / "outputs" / "figures"
RES = ROOT / "outputs" / "results"
MODELS = ROOT / "outputs" / "models"
SEEDS = [0, 1, 2]

for p in (DATA_RAW, DATA_PROC, FIG, RES, MODELS):
    p.mkdir(parents=True, exist_ok=True)


def set_seed(seed: int = 0) -> None:
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def save_result(name: str, obj: dict) -> Path:
    """Every number used in the README or report must be saved through this function."""
    path = RES / f"{name}.json"
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, default=float)
    return path
