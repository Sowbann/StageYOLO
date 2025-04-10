from ultralytics import YOLO
import os

# Charger un modèle préentraîné (ex : COCO ou ton modèle custom)
model = YOLO("yolov8m.pt")  # ou "yolo11m_custom.pt" si déjà entraîné sur ton domaine

# Dossier contenant les images à annoter
image_dir = "/home/alguerraquadrado/datasets/test/"
output_dir = image_dir  # les labels seront sauvegardés à côté des images

# Inférer sur chaque image individuellement
for img_file in os.listdir(image_dir):
    if img_file.endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(image_dir, img_file)
        results = model(image_path)

        # Récupérer les prédictions pour cette image
        for result in results:
            name, _ = os.path.splitext(img_file)
            label_path = os.path.join(output_dir, name + ".txt")

            with open(label_path, "w") as f:
                for box in result.boxes:
                    cls = int(box.cls.item())  # classe prédite
                    xywhn = box.xywhn[0]       # boîte au format [x_center, y_center, width, height] normalisé
                    line = f"{cls} {xywhn[0].item():.6f} {xywhn[1].item():.6f} {xywhn[2].item():.6f} {xywhn[3].item():.6f}\n"
                    f.write(line)

