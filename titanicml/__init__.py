"""
Module titanicml.

Ce module contient les fonctions et classes pour le projet Titanic ML.
"""

from .data.import_data import (
    load_data,
    explore_data
)
from .features.build_features import (
    preprocess_data
)
from .models.train_evaluate import (
    train_model,
    evaluate_model
)
__all__ = [
    "load_data",
    "explore_data",
    "preprocess_data",
    "train_model",
    "evaluate_model"
]