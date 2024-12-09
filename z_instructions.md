### GitHub
> repo name `seedboxes-models` [link](https://github.com/viestursja/seedboxes_models)



### This for model building process -Detectation

1. On [cvat.ai](https://www.cvat.ai/) annotate the model
2. Export as Yolo 1.1 . I did not try Yolov8 detection/segmentation versions. File will contain images in '/object_train_data' and labels in 'train.txt'
3. Train the model with  `training_the_model.py` setting the config params in yaml file. onnx version has to be 1.8.0 !!!
4. Training output `best.pt` to be converted to `onnx` format by 'pt_to_onnx.py'
5. `onnx` is used furthet to convert to `.hef` for Hailo applications


### Pose Estimation

#### Sources:

[Roboflow Blog: Piemērs, iznatojot Roboflow](https://blog.roboflow.com/train-a-custom-yolov8-pose-estimation-model/)

[Bulgārs YT](https://www.youtube.com/watch?v=gA5N54IO1ko&ab_channel=Computervisionengineer)

[COCO Dataset format-data](https://www.youtube.com/watch?v=gA5N54IO1ko&ab_channel=Computervisionengineer)

---

#### Process

> in CVAT job use 'Draw new points' + 'Draw new rectangle' "Label" abiem ir vienādi? Vai box labāk ir sagriezt?

> Save the job and export as 'CVAT for images 1:1' - it will be in .xml format

> Konverē uz xml uz yolo formātu ar skriptu `/4_pose_estiimation/cvat_to_ultralitics_yolov8.py` : iegūst katram img atbolstošu .txt failu

> .yaml config fails par flip_idx parametru ChatGPT [šeit](https://chatgpt.com/c/675466eb-a8e4-800d-8b87-d64a260af236)

> `model.train()` [parametru settings](https://docs.ultralytics.com/modes/train/#augmentation-settings-and-hyperparameters)

> CLI komanda: `yolo task=pose mode=train data=".\data.yaml" model=yolov8n.pt imgsz=640`