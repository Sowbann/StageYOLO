import json
import yaml

# === Chemins ===
coco_json_path = "/home/alguerraquadrado/datasets/TACO/data/annotations.json"  # fichier COCO
train_images_path = "/home/alguerraquadrado/datasets/TACO/data/labels"  # dossier où sauver les fichiers .txt
val_images_path = "/home/alguerraquadrado/datasets/TACO/data/"               # racine où sont stockées les images

# Charger les catégories du fichier COCO
with open(coco_json_path, "r") as f:
    coco = json.load(f)

category_names = [cat["name"] for cat in coco["categories"]]

# Création du dictionnaire YAML
yaml_dict = {
    "train": train_images_path,
    "val": val_images_path,
    "nc": len(category_names),
    "names": category_names
}

# Sauvegarde dans un fichier YAML
output_yaml_path = "dataset_waste.yaml"
with open(output_yaml_path, "w") as f:
    yaml.dump(yaml_dict, f, sort_keys=False)

print(f"✅ Fichier '.yaml' généré avec {len(category_names)} classes.")
