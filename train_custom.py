from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11m_custom.pt")

# Train the model using the 'dataset_custom.yaml' dataset for x epochs
model.train(data="dataset_custom.yaml", epochs=20, imgsz = 640, batch = 128, workers=7)
