# 📊 But du stage

Ce repository contient les fichiers et scripts associés à l'utilisation de plusieurs datasets, destinés à la classification des trous de route et des déchets.

Nous utilisons **Ultralytics YOLO** pour la classification :  
👉 https://github.com/ultralytics/ultralytics

---

## 📁 Contenu

Les datasets utilisés (vous n'etes pas obligé de les telecharger un a un):

- **TACO** (dataset de déchets) : https://github.com/pedropro/TACO
- **RDD_SPLIT** (dataset de routes abîmées) : https://www.kaggle.com/datasets/aliabdelmenam/rdd-2022
- **augmenteTACO** (dataset de déchets, basé sur TACO augmenté grâce à `augmentation.py`)

---

## Utilisation

Selon le training que vous voulez effectué, modifier le fichier pour mettre les parametres(model a utiliser, nombre d'epoch, etc...) que vous souhaitez dans script/ :
train_road.py pour les routes
train_waste.py pour les dechets

Pour lancer un training, un scrit slurm est disponible dans script/train.slurm
Il vous faut decommenté ce que vous voulez faire et changer les liens des fichiers selon votre architecture 

---

## Resultat 

Un fichier resultat est disponible avec son model et le resultat de son entrainement
Lorsqu'il y a ecrit yy_versionXX, cela veut dire que c'est la version du model yy avec XX nombre d'epoch

Vous pouvez aussi retrouver l'entiereté de l'entrainement dans runs/anciens/ pour chaque model 

---

## 📥 Téléchargement des datasets

Le dataset complet est disponible en téléchargement via le lien suivant disponible jusqu'au 13/07:

👉 [Télécharger datasets](https://exemple.com/chemin/vers/le/dataset.zip)

Une fois téléchargé, vous pouvez l'extraire avec la commande suivante :

```bash
unzip datasets.zip -d ./datasets