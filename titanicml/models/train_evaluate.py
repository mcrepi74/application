# train_evaluate.py
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from titanicml import preprocess_data
import os
import yaml
from loguru import logger
import joblib

# Récupérer le chemin absolu du dossier contenant ce script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_PATH = os.path.join(BASE_DIR, "configuration", "config.yaml")

# Charger le fichier de configuration
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)


def train_model(X_train, y_train, n_trees):
    """Entraîne un modèle RandomForest et sauvegarde le modèle."""
    try:
        if n_trees < 1:
            raise ValueError("Le nombre d'arbres doit être supérieur à 0")
        logger.info(f"Début de l'entraînement avec {n_trees} arbres...")

        # Prétraitement et pipeline
        preprocessor = preprocess_data()
        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(n_estimators=n_trees, random_state=config["model"]["random_state"])),
        ])

        # Entraîner le modèle
        pipe.fit(X_train, y_train)
        logger.success("Modèle entraîné avec succès")

        # Sauvegarder le modèle au format joblib
        model_path = os.path.join(BASE_DIR, "model.joblib")
        joblib.dump(pipe, model_path)
        logger.info(f"Modèle sauvegardé sous {model_path}")

        return pipe
    except Exception as e:
        logger.error(f"Erreur lors de l'entraînement du modèle: {e}")
        raise


def evaluate_model(model, X_test, y_test):
    """Évalue le modèle et affiche les résultats."""
    test_score = model.score(X_test, y_test)
    logger.info(f"{test_score:.1%} de bonnes réponses sur les données de test")
    logger.info("-" * 20)
    logger.info("Matrice de confusion :")
    logger.info(confusion_matrix(y_test, model.predict(X_test)))
