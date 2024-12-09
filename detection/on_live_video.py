# this run son windows cpu!

import cv2
from ultralytics import YOLO

# Path to your YOLOv8 model
model_path = r'C:\Users\viest\OneDrive\z_old\Desktop\sandbox\25_model_building_boxes\detection\last.pt'
model = YOLO(model_path)

# Initialize video capture (0 for the default camera)
cap = cv2.VideoCapture(0)

# VideoWriter to save the output if needed
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Set a confidence threshold for displaying boxes
threshold = 0.75

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # Predict using YOLOv8 model
    results = model(frame)[0]

    # Iterate over detected objects
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        # Only draw boxes if confidence is above the threshold
        if score > threshold:
            # Draw bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
            # Put the label and score
            cv2.putText(frame, f'{results.names[int(class_id)].upper()} {score:.2f}', 
                        (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

    # Show the frame
    cv2.imshow('YOLOv8 Live Stream', frame)

    # Save the frame to video file
    # out.write(frame)

    # Press 'q' to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and writer
cap.release()
# out.release()
cv2.destroyAllWindows()
