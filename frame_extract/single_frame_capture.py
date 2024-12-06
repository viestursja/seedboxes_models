import cv2 as cv
import os

capture = cv.VideoCapture(0)

save_path = 'saved_frames' 

if not os.path.exists(save_path):
    os.makedirs(save_path)

counter = 0

while True:
    ok, frame = capture.read()
    cv.imshow('video', frame)
    # time.sleep(0.5)
    # cv.waitKey(500)

    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('z'):
        image_path = 'captured_image_' + str(counter) + '.jpg'
        cv.imwrite(image_path, frame)
        counter = counter + 1
        print(f'Captured {counter}')


capture.release()
cv.destroyAllWindows()