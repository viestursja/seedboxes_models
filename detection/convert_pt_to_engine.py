from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("detection\last.pt")

# Export the model to TensorRT
model.export(format="engine")  # creates 'yolo11n.engine' file and yolo11.onnx files