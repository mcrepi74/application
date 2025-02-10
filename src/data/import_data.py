import pandas as pd
import yaml

config = yaml.safe_load(open("configuration/config.yaml"))

def load_data(file_path):
    """Charge les données à partir d'un fichier CSV."""
    return pd.read_csv(file_path)

def explore_data(df):
    """Affiche un aperçu des données et les valeurs manquantes."""
    print(df.head())
    print(df.isnull().sum())
