#!/bin/bash
# filepath: app/run.sh

set -e

echo "==> Entraînement du modèle"
python train.py

echo "==> Lancement de l'API FastAPI"
uvicorn app.api:app --host 0.0.0.0 --port 8000
