### This for model building process

1. On [cvat.ai](https://www.cvat.ai/) annotate the model
2. Export as Yolo 1.1 . I did not try Yolov8 detection/segmentation versions. File will contain images in '/object_train_data' and labels in 'train.txt'
3. Train the model with  `training_the_model.py` setting the config params in yaml file. onnx version has to be 1.8.0 !!!
4. Training output `best.pt` to be converted to `onnx` format by 'pt_to_onnx.py'
5. `onnx` is used furthet to convert to `.hef` for Hailo applications
