import os
import shutil
import random

source_dir = "../datasets/TACO/data/"  # dossier contenant les batchs
output_dir = "../datasets/TACO/dataYOLO/"

all_pairs = []

# Crée les dossiers de sortie
for split in ['images/train', 'images/val', 'labels/train', 'labels/val']:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Récupère toutes les images et labels de tous les batchs avec renommage unique
global_counter = 0
for batch_id in range(1, 16):
    img_dir = os.path.join(source_dir, f"batch_{batch_id}")
    lbl_dir = os.path.join(source_dir, f"batch_{batch_id}", "labels")

    if not os.path.exists(img_dir) or not os.path.exists(lbl_dir):
        continue

    for img_file in os.listdir(img_dir):
        if img_file.endswith(('.jpg', '.jpeg', '.png')):
            base_name = f"img_{global_counter:05d}"
            img_ext = os.path.splitext(img_file)[1]
            new_img_name = base_name + img_ext
            new_lbl_name = base_name + ".txt"

            img_path = os.path.join(img_dir, img_file)
            lbl_path = os.path.join(lbl_dir, img_file.rsplit(".", 1)[0] + ".txt")

            if not os.path.exists(lbl_path):
                continue  # ignore images sans label

            all_pairs.append(((img_path, new_img_name), (lbl_path, new_lbl_name)))
            global_counter += 1

# Shuffle et split (80% train / 20% val)
random.shuffle(all_pairs)
split_index = int(len(all_pairs) * 0.8)
train_set = all_pairs[:split_index]
val_set = all_pairs[split_index:]

def copy_pairs(pairs, img_out, lbl_out):
    for (img_src, img_name), (lbl_src, lbl_name) in pairs:
        shutil.copy(img_src, os.path.join(output_dir, img_out, img_name))
        shutil.copy(lbl_src, os.path.join(output_dir, lbl_out, lbl_name))

copy_pairs(train_set, "images/train", "labels/train")
copy_pairs(val_set, "images/val", "labels/val")

print(f"✅ Organisation terminée : {len(train_set)} images train, {len(val_set)} images val.")
