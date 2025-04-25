import bettercam
import time
import cv2
import numpy as np

# Initialize camera
camera = bettercam.create()

# Set region: 640x640 center of a 1920x1080 screen
left, top = (1920 - 640) // 2, (1080 - 640) // 2
right, bottom = left + 640, top + 640
region = (left, top, right, bottom)

frame_count = 0
start_time = time.time()
fps = 0

try:
    while True:
        frame = camera.grab(region=region)

        if frame is None:
            continue  # Skip frame if no update

        frame_count += 1
        elapsed = time.time() - start_time

        if elapsed >= 1.0:
            fps = frame_count
            frame_count = 0
            start_time = time.time()

        
        # # Draw FPS text on frame
        # cv2.putText(
        #     frame,
        #     f"FPS: {fps}",
        #     (10, 30),
        #     cv2.FONT_HERSHEY_SIMPLEX,
        #     1,
        #     (0, 255, 0),
        #     2,
        #     cv2.LINE_AA
        # )

        # # Display the frame
        # cv2.imshow("BetterCam 640x640", frame)

        # # Quit with 'q'
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        
            print(f"FPS: {fps}")

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    cv2.destroyAllWindows()
