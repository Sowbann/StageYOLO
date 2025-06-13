# 🎯 Objectif du Stage

Ce repository contient les fichiers et scripts associés à l'utilisation de plusieurs datasets, destinés à la **classification des trous de route** et des **déchets** à l’aide du framework **Ultralytics YOLO**.

🔗 YOLO : https://github.com/ultralytics/ultralytics

---

## 📚 Datasets utilisés

Vous n’avez pas besoin de les télécharger un à un, un lien de téléchargement global est fourni plus bas.

- 🗑️ **TACO** (déchets) : https://github.com/pedropro/TACO  
- 🛣️ **RDD_SPLIT** (routes abîmées) : https://www.kaggle.com/datasets/aliabdelmenam/rdd-2022  
- 🧪 **augmenteTACO** (déchets augmentés via `augmentation.py`, basé sur TACO)  

---

## ⚙️ Utilisation

### 📂 Choix du training

Modifiez les fichiers situés dans `script/` pour ajuster les paramètres du modèle, le nombre d’époques, la taille des images, etc. :

- `train_road.py` ➜ pour l’entraînement sur **routes**
- `train_waste.py` ➜ pour l’entraînement sur **déchets**

### 🚀 Lancer un job SLURM

Un script SLURM est fourni pour lancer les entraînements :  
📄 `script/train.slurm`

Dans ce script :
- Décommentez la section correspondant au training souhaité
- Adaptez les chemins de fichiers à votre infrastructure (chemins absolus, envs, etc.)

---

## ✅ Résultats

Les résultats d’entraînement sont organisés de la manière suivante :

- 📁 `resultat/` ➜ contient les modèles finaux et un résumé des performances
  - Exemple : `yy_versionXX` = modèle YOLO **yy**, entraîné sur **XX époques**
- 📁 `runs/anciens/` ➜ archive complète de tous les entraînements précédents (logs, modèles, graphiques)

---

## 📥 Téléchargement des Datasets

Les datasets sont regroupés dans une seule archive disponible jusqu’au **13/07/2025** :

👉 [Télécharger datasets](https://filesender.renater.fr/?s=download&token=274dad06-9be0-4c27-9d0f-7709f38862f2)

Après téléchargement, décompressez-les avec :

```bash
unzip datasets.zip -d ./datasets
