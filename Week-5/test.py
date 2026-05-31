from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Run prediction on test images
results = model.predict(
    source="test_images",
    save=True,
    imgsz=384,
    conf=0.25
)

print("Prediction completed!")
