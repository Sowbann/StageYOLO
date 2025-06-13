#!/bin/bash
#SBATCH --job-name=yolo_train       # Nom du job
#SBATCH --output=output30.log         # Fichier de sortie (stdout)
#SBATCH --error=error30.log           # Fichier d'erreur (stderr)
#SBATCH --partition=mesonet         # Partition (choisis celle de ton cluster)
#SBATCH -N 1                        # Nombre de nœuds (ici, 1 nœud)
#SBATCH -c 90                      # Nombre de cœurs CPU
#SBATCH --gres=gpu:6                # Nombre de GPU nécessaires
#SBATCH --time=7:00:00              # Durée maximale du job (ici 7 heures)
#SBATCH --mem=300G                  # Mémoire demandée (ici 500 Go)
#SBATCH --account=m25008            # Compte Slurm pour le billing

# Choix
#python3 /home/alguerraquadrado/StageYOLO/script/train_waste.py
#python3 /home/alguerraquadrado/StageYOLO/script/train_road.py
