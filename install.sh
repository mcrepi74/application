#!/bin/bash

echo "🚀 Initialisation de l'installation..."

# Mettre à jour les paquets
sudo apt update && sudo apt upgrade -y

# Installer Python et venv si non installés
sudo apt install -y python3 python3-venv python3-pip

# Créer et activer l’environnement virtuel
python3 -m venv titanic
source titanic/bin/activate

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements_clean.txt

echo "✅ Installation terminée !"
echo "Pour exécuter votre script :"
echo "1️⃣ Activez l'environnement : source titanic/bin/activate"
echo "2️⃣ Lancez main.py : python main.py"
