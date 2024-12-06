import cv2 as cv
# import time
import os

capture = cv.VideoCapture(0)

SCALE = 0.75

# Define parameters
n = 10  # Save every n-th frame
blur_threshold = 300  # Define the threshold for blur level (higher means sharper)

frame_count = 0  # To count frames
save_path = 'saved_frames'  # Directory to save the frames

def resizeFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

if not os.path.exists(save_path):
    os.makedirs(save_path)

def calculate_blur(frame):
    """Calculate the Laplacian variance of the frame to detect blur."""
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Convert to grayscale
    laplacian_var = cv.Laplacian(gray, cv.CV_64F).var()  # Get Laplacian variance
    return laplacian_var

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#     resized = resizeFrame(frame, 0.2)
#     cv.imshow('video_2', resized)
#     if cv.waitKey(20) & 0xFF == ('d'):
#         break

while True:
    ok, frame = capture.read()
    cv.imshow('video', frame)
    # time.sleep(0.5)
    # cv.waitKey(500)
    if cv.waitKey(20) & 0xFF == ('d'):
        break

    # Check if it's the n-th frame
    frame_count += 1
    if frame_count % n == 0:
        # Calculate blur level
        blur_level = calculate_blur(frame)
        print(f"Frame {frame_count}: Blur Level = {blur_level}")

        # If the blur level is above the threshold, save the frame
        if blur_level > blur_threshold:
            # Save the frame as a .jpg file
            filename = f"{save_path}frame_{frame_count}.jpg"
            cv.imwrite(filename, frame)
            print(f"Frame {frame_count} saved as {filename}")

    # Exit if 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()