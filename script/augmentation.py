import albumentations as A
import cv2
import os

# Définir une série de transformations
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.Rotate(limit=15, p=0.5),
    A.Blur(blur_limit=3, p=0.2),
], bbox_params=A.BboxParams(
    format='yolo',
    label_fields=['class_labels'],
    check_each_transform=False,
    min_visibility=0.1
))

def clamp_bbox(bbox):
    return [max(0.0, min(1.0, x)) for x in bbox]

def augment_yolo_image(image_path, label_path, output_image_path, output_label_path):
    # Charger image et labels
    image = cv2.imread(image_path)
    h, w, _ = image.shape

    with open(label_path, 'r') as f:
        lines = f.readlines()
    
        # Lire les bounding boxes
    bboxes = []
    class_labels = []
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        x_center, y_center, width, height = map(float, parts[1:])
        bboxes.append(clamp_bbox([x_center, y_center, width, height]))
        class_labels.append(class_id)


    # Appliquer la transformation
    transformed = transform(image=image, bboxes=bboxes, class_labels=class_labels)
    aug_img = transformed['image']

    aug_bboxes = []
    aug_labels = []
    for label, bbox in zip(transformed['class_labels'], transformed['bboxes']):
        # Clamp les bboxes après transformation
        bbox = clamp_bbox(bbox)
        if all(0.0 <= coord <= 1.0 for coord in bbox):
            aug_bboxes.append(bbox)
            aug_labels.append(label)


    if not aug_bboxes:
        print(f"Skipping {image_path}: no valid bboxes after augmentation.")
        return

    # Sauvegarder nouvelle image
    cv2.imwrite(output_image_path, aug_img)

    # Sauvegarder les nouveaux labels
    with open(output_label_path, 'w') as f:
        for label, bbox in zip(aug_labels, aug_bboxes):
            f.write(f"{label} {' '.join(map(str, bbox))}\n")


input_images = "../datasets/TACO/dataYOLO/images/val"
input_labels = "../datasets/TACO/dataYOLO/labels/val"
output_images = "../datasets/augmenteTACO/images/val"
output_labels = "../datasets/augmenteTACO/labels/val"

os.makedirs(output_images, exist_ok=True)
os.makedirs(output_labels, exist_ok=True)

started = False  # Flag pour savoir quand commencer

for filename in sorted(os.listdir(input_images)):
    if filename.endswith('.jpg'):
        name = filename.split('.')[0]
        
        # On ne commence qu'à partir de img_00156
        if not started:
            if name < "img_00260":
                continue
            else:
                started = True  # On a atteint l'image seuil

        image_path = os.path.join(input_images, filename)
        label_path = os.path.join(input_labels, f"{name}.txt")

        for i in range(3):  # créer 3 augmentations par image
            out_img = os.path.join(output_images, f"{name}_aug{i}.jpg")
            out_lbl = os.path.join(output_labels, f"{name}_aug{i}.txt")
            augment_yolo_image(image_path, label_path, out_img, out_lbl)



