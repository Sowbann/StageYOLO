from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo11m_custom.pt")

# Train the model using the 'dataset_custom.yaml' dataset for x epochs
model.train(data="dataset_waste.yaml", epochs=50, imgsz = 640, batch = 64, workers=8)
