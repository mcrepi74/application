from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import os
import yaml

# Récupérer le chemin absolu du dossier contenant ce script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_PATH = os.path.join(BASE_DIR, "configuration", "config.yaml")

# Charger le fichier de configuration
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)


def preprocess_data():
    """Crée un pipeline de prétraitement des données."""
    numeric_features = ["Age", "Fare"]
    categorical_features = ["Embarked", "Sex"]

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy=config["preprocessing"]["imputation_strategy"])),
            ("scaler", MinMaxScaler() if config["preprocessing"]["scale_features"] else "passthrough"),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy=config["preprocessing"]["categorical_imputation"])),
            ("onehot", OneHotEncoder()),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    return preprocessor
