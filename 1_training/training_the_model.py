

# set parameters on config.yaml
# onnx version has to be 1.8.0: pip install onnx==1.8.0

from ultralytics import YOLO


# Load a model
model = YOLO("yolov8s.pt")

# Train the model
train_results = model.train(
    data=r"C:\Users\viest\OneDrive\z_old\Desktop\sandbox\25_model_building_boxes\1_training\config.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=640,  # training image size
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)
