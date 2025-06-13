from ultralytics import YOLO

model = YOLO("yolo11m_custom.pt")

model.train(data="dataset_waste.yaml", epochs=30, imgsz = 640, batch = 64, workers=32)
