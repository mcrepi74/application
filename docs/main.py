import argparse
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
import os
import sys
import yaml
from loguru import logger
import warnings
import pandas as pd
from pandas.core.common import SettingWithCopyWarning

# Filter warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=SettingWithCopyWarning)
pd.options.mode.chained_assignment = None

# Ajouter le répertoire parent au sys.path pour trouver le module titanicml
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from titanicml.data.import_data import load_data, explore_data
from titanicml.models.train_evaluate import train_model, evaluate_model

# Ajouter un fichier de log avec rotation automatique
logger.add("logs/app.log", rotation="10 MB", level="INFO")

# Remplacer le code existant de configuration du chemin par:
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'configuration', 'config.yaml')
if not os.path.exists(CONFIG_PATH):
    # Fallback path pour Docker
    CONFIG_PATH = os.path.join('/titanic', 'configuration', 'config.yaml')
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Le fichier config.yaml n'a pas été trouvé ni dans {CONFIG_PATH}")

logger.info(f"Utilisation du fichier de configuration: {CONFIG_PATH}")

# Charger la configuration
def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

config = load_config()

# Charger les variables d'environnement
load_dotenv()
jeton_api = os.environ.get("JETON_API", "")

if jeton_api.startswith("$"):
    logger.success("API token has been configured properly")
else:
    logger.warning("API token has not been configured")

def main():
    """Exécute le pipeline d'analyse et de modélisation."""
    parser = argparse.ArgumentParser(description="Paramétrisation du nombre d'arbres pour RandomForest.")
    parser.add_argument("--n_trees", type=int, default=config["model"]["n_trees"], help="Nombre d'arbres pour RandomForest")
    args = parser.parse_args()
    logger.info(f"Nombre d'arbres utilisé: {args.n_trees}")

    df = load_data(config["data"]["full_data_path"])
    explore_data(df)

    # Visualisation
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.countplot(data=df, x="Pclass", ax=axes[0]).set_title("Fréquence des Pclass")
    sns.barplot(data=df, x="Pclass", y="Survived", ax=axes[1]).set_title("Survie des Pclass")
    plt.show()

    sns.histplot(data=df, x="Age", bins=15, kde=False).set_title("Distribution de l'âge")
    plt.show()

    # Préparation des données
    y = df["Survived"]
    X = df.drop("Survived", axis="columns")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config["model"]["test_size"], random_state=config["model"]["random_state"])

    model = train_model(X_train, y_train, args.n_trees)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
