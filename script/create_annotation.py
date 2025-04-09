from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11m_custom.pt")

results = model('/home/alguerraquadrado/datasets/')  # Remplace par le chemin vers tes images

# Générer un fichier d'annotations au format YOLO pour chaque image
results.save()  # Sauvegarder les résultats sous forme de fichiers d'annotations