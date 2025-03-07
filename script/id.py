import os
from collections import Counter

annotations_path = "../datasets/RDD_SPLIT/test/labels/"  # Dossier contenant les fichiers .txt
class_counts = Counter()

for file in os.listdir(annotations_path):
    if file.endswith(".txt"):
        with open(os.path.join(annotations_path, file), "r") as f:
            for line in f:
                class_id = int(line.split()[0])  # Extraire le premier élément de la ligne
                class_counts[class_id] += 1

print("Classes détectées :", sorted(class_counts.keys()))
