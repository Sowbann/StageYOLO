import json
import os

# === Chemin du fichier COCO commun ===
coco_json_path = "/home/alguerraquadrado/datasets/TACO/data/annotations.json"

# === Charger le fichier JSON une seule fois ===
with open(coco_json_path, 'r') as f:
    coco = json.load(f)

# === Mappings ===
image_id_map = {img["id"]: img for img in coco["images"]}
categories = coco["categories"]
cat2yolo = {cat["id"]: idx for idx, cat in enumerate(categories)}

# === Boucle sur les batches ===
for batch_id in range(3, 16):  # De batch_3 à batch_15
    print(f"🔄 Traitement du batch_{batch_id}...")

    output_labels_dir = f"/home/alguerraquadrado/datasets/TACO/data/batch_{batch_id}/labels"
    os.makedirs(output_labels_dir, exist_ok=True)

    labels = {}
    for ann in coco["annotations"]:
        img_id = ann["image_id"]
        image_info = image_id_map[img_id]
        
        # Vérifier si cette image est dans le batch courant
        if f"batch_{batch_id}/" not in image_info["file_name"]:
            continue

        category_id = ann["category_id"]
        bbox = ann["bbox"]
        img_w, img_h = image_info["width"], image_info["height"]
        img_filename = os.path.basename(image_info["file_name"])
        txt_filename = os.path.splitext(img_filename)[0] + ".txt"

        # Convertir bbox au format YOLO
        x, y, w, h = bbox
        x_center = (x + w / 2) / img_w
        y_center = (y + h / 2) / img_h
        w /= img_w
        h /= img_h

        yolo_class = cat2yolo[category_id]
        label_line = f"{yolo_class} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}"

        if txt_filename not in labels:
            labels[txt_filename] = []
        labels[txt_filename].append(label_line)

    # Sauvegarder les fichiers YOLO
    for txt_file, lines in labels.items():
        txt_path = os.path.join(output_labels_dir, txt_file)
        with open(txt_path, 'w') as f:
            f.write("\n".join(lines))

    print(f"✅ Batch_{batch_id} : {len(labels)} fichiers générés dans {output_labels_dir}")

print("🎉 Conversion terminée pour tous les batches !")
