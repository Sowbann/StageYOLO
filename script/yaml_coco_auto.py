import json
import yaml
import os

# === Chemin vers le fichier COCO contenant les catégories ===
coco_json_path = "/home/alguerraquadrado/datasets/TACO/data/annotations.json"

# Charger les catégories du fichier COCO
with open(coco_json_path, "r") as f:
    coco = json.load(f)

category_names = [cat["name"] for cat in coco["categories"]]

# Chemins d'images et de labels combinés pour tous les batches
all_train_images_path = []
all_val_images_path = []
all_train_labels_path = []

# Boucle sur batch_1 à batch_15
for batch_id in range(1, 16):
    batch_name = f"batch_{batch_id}"
    print(f"🔧 Génération des chemins pour {batch_name}...")

    # Définir les chemins pour ce batch
    train_labels_path = f"/home/alguerraquadrado/datasets/TACO/data/{batch_name}/labels"
    val_images_path = f"/home/alguerraquadrado/datasets/TACO/data/{batch_name}/images"
    
    # Vérifie que les chemins existent
    if not os.path.exists(train_labels_path) or not os.path.exists(val_images_path):
        print(f"⚠️  Chemins manquants pour {batch_name}, ignoré.")
        continue

    # Ajouter les chemins dans les listes globales
    all_train_labels_path.append(train_labels_path)
    all_val_images_path.append(val_images_path)
    all_train_images_path.append(val_images_path)  # Utiliser les mêmes images pour train et val dans ce cas

# Créer le dictionnaire YAML avec tous les batches
yaml_dict = {
    "train": all_train_images_path,
    "val": all_val_images_path,
    "nc": len(category_names),
    "names": category_names
}

# Sauvegarder le fichier .yaml final
output_yaml_path = "dataset_waste.yaml"
with open(output_yaml_path, "w") as f:
    yaml.dump(yaml_dict, f, sort_keys=False)

print(f"✅ Fichier '.yaml' combiné généré : {output_yaml_path}")
