import os
import yaml

train_dir = '/home/alguerraquadrado/datasets/train'
val_dir = '/home/alguerraquadrado/datasets/test'

# Déduire les classes depuis les sous-dossiers du dossier train
classes = sorted(os.listdir(train_dir))
num_classes = len(classes)

data_yaml = {
    'train': train_dir,
    'val': val_dir,
    'nc': num_classes,
    'names': classes
}

with open('dataset_waste_auto.yaml', 'w') as f:
    yaml.dump(data_yaml, f)

print("Fichier dataset.yaml généré avec succès.")
