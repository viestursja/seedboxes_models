from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO(r"C:\Users\viest\OneDrive\z_old\Desktop\sandbox\25_model_building_boxes\runs\detect\train\weights\best.pt")

# Export the model to ONNX format
model.export(format="onnx")  # creates 'yolov8n.onnx'
