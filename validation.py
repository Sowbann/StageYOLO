from ultralytics import YOLO

# Charger votre modèle
model = YOLO('version2.pt')

# Évaluer le modèle sur l'ensemble de validation
results = model.val(data='dataset_custom.yaml')

# Afficher les métriques
print(results.mean_results())  # Affiche les valeurs moyennes des métriques