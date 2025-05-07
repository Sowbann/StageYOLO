#!/bin/bash
#SBATCH --job-name=yolo_test10       # Nom du job
#SBATCH --output=output10.log         # Fichier de sortie (stdout)
#SBATCH --error=error10.log           # Fichier d'erreur (stderr)
#SBATCH --partition=mesonet         # Partition (choisis celle de ton cluster)
#SBATCH -N 1                        # Nombre de nœuds (ici, 1 nœud)
#SBATCH -c 32                      # Nombre de cœurs CPU
#SBATCH --gres=gpu:1                # Nombre de GPU nécessaires
#SBATCH --time=7:00:00              # Durée maximale du job (ici 7 heures)
#SBATCH --mem=200G                  # Mémoire demandée (ici 500 Go)
#SBATCH --account=m25008            # Compte Slurm pour le billing

# Lancement du test 
yolo detect predict model=/resultat/road_version10.pt source=../datasets/RDD_SPLIT/test/images