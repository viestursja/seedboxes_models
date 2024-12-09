from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("best_seedbox_v2.pt")

# Export the model to TensorRT
model.export(format="engine")  # creates 'yolo11n.engine' file and yolo11.onnx files

# # Load the exported TensorRT model
# trt_model = YOLO("yolo11n.engine")

# # Run inference
# results = trt_model("https://ultralytics.com/images/bus.jpg")
