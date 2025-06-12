# Étape 1 : Utiliser une image officielle avec Ubuntu 22.04
FROM ubuntu:22.04

# Installer Python et les dépendances nécessaires
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    apt-get clean

# Étape 2 : Définir le dossier de travail dans le conteneur
WORKDIR /titanic

# Étape 3 : Copier les fichiers nécessaires dans l'image Docker
COPY app ./app
COPY requirements_clean.txt ./
COPY titanicml/ ./titanicml/
COPY configuration/ ./configuration/
COPY docs/train.py ./ 


# Étape 4 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements_clean.txt

# Étape 5 : Définir la commande à exécuter
CMD ["bash", "-c", "./app/run.sh"]