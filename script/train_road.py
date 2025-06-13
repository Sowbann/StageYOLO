from ultralytics import YOLO

model = YOLO("yolo11m_custom.pt")

model.train(data="dataset_road.yaml", epochs=40, imgsz = 640, batch = 256, workers=32)
