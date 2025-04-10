import json
import os

# === Chemins ===
coco_json_path = "/home/alguerraquadrado/datasets/TACO/data/annotations.json"  # fichier COCO
output_labels_dir = "/home/alguerraquadrado/datasets/TACO/data/labels"  # dossier où sauver les fichiers .txt
images_dir = "/home/alguerraquadrado/datasets/TACO/data/"               # racine où sont stockées les images

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_labels_dir, exist_ok=True)

# Charger le fichier JSON
with open(coco_json_path, 'r') as f:
    coco = json.load(f)

# Créer un mapping ID → image filename / taille
image_id_map = {img["id"]: img for img in coco["images"]}

# Créer un mapping COCO category_id → 0-N (YOLO)
categories = coco["categories"]
cat2yolo = {cat["id"]: idx for idx, cat in enumerate(categories)}

# Générer un .txt par image
labels = {}
for ann in coco["annotations"]:
    img_id = ann["image_id"]
    category_id = ann["category_id"]
    bbox = ann["bbox"]  # COCO: [top-left-x, top-left-y, width, height]

    # Récupérer l'image correspondante
    image_info = image_id_map[img_id]
    img_w, img_h = image_info["width"], image_info["height"]
    img_filename = os.path.basename(image_info["file_name"])
    txt_filename = os.path.splitext(img_filename)[0] + ".txt"

    # Convertir bbox en format YOLO (normalisé)
    x, y, w, h = bbox
    x_center = (x + w / 2) / img_w
    y_center = (y + h / 2) / img_h
    w /= img_w
    h /= img_h

    yolo_class = cat2yolo[category_id]
    label_line = f"{yolo_class} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}"

    # Stocker dans un fichier
    if txt_filename not in labels:
        labels[txt_filename] = []
    labels[txt_filename].append(label_line)

# Écriture des fichiers .txt
for txt_file, lines in labels.items():
    txt_path = os.path.join(output_labels_dir, txt_file)
    with open(txt_path, 'w') as f:
        f.write("\n".join(lines))

print(f"✅ Conversion terminée : {len(labels)} fichiers générés dans {output_labels_dir}")
