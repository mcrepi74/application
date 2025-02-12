import pandas as pd
import os
import yaml

# Récupérer le chemin absolu du dossier contenant ce script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_PATH = os.path.join(BASE_DIR, "configuration", "config.yaml")

# Charger le fichier de configuration
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)


def load_data(file_path):
    """Charge les données à partir d'un fichier CSV."""
    return pd.read_csv(file_path)

def explore_data(df):
    """Affiche un aperçu des données et les valeurs manquantes."""
    print(df.head())
    print(df.isnull().sum())
