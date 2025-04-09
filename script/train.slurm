#!/bin/bash
#SBATCH --job-name=yolo_train       # Nom du job
#SBATCH --output=output.log         # Fichier de sortie (stdout)
#SBATCH --error=error.log           # Fichier d'erreur (stderr)
#SBATCH --partition=mesonet         # Partition (choisis celle de ton cluster)
#SBATCH -N 1                        # Nombre de nœuds (ici, 1 nœud)
#SBATCH -c 112                      # Nombre de cœurs CPU
#SBATCH --gres=gpu:8                # Nombre de GPU nécessaires
#SBATCH --time=7:00:00              # Durée maximale du job (ici 7 heures)
#SBATCH --mem=1000G                  # Mémoire demandée (ici 500 Go)
#SBATCH --account=m25008            # Compte Slurm pour le billing

# Lancement de ton entraînement
# python3 /home/alguerraquadrado/StageYOLO/script/train_road.py

python3 /home/alguerraquadrado/StageYOLO/script/create_annotation.py
