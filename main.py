import cv2
import HandTrackingModule as htm
import api_calls as api
import time
from CircularLinkedList import CircularLinkedList
import numpy as np

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
calls = api.API_Calls()
brightness = 100
last_request_time = time.time()  # Tracks the last API call
rate_limit_interval = 2  # Minimum time interval (seconds) between requests
global color_index
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_list = CircularLinkedList(colors)

color_index = 0
cooldown_time = 1.0  # Cooldown time in seconds
last_swipe_time = time.time()

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)


    if hands:
        hand1 = hands[0]
        palm_x = hand1["palm_center"][0]

        fingers1 = detector.fingersUp(hand1)
        num_fingers = sum(fingers1)
        new_brightness = num_fingers * 20  # Map fingers (1-5) to brightness (20-100)
        current_time = time.time()

        if brightness == 0:
            # Ensure the image is not None before processing
            if img is not None:
                img = 255 * np.ones_like(img)  # White image
                cv2.putText(
                    img,
                    "Lights are off. Here's some light to capture the gesture.",
                    (50, img.shape[0] // 2),  # Properly use img.shape[0] for height
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 0),  # Black text
                    2
                )

        # Send API call only if brightness changes and rate-limit allows
        # if new_brightness != brightness and (time.time() - last_request_time) > rate_limit_interval:
        #     brightness = new_brightness
        #     print(f"Setting Brightness: {brightness}")
        #     calls.set_brightness(brightness)
        #     last_request_time = time.time()


        # current_time = time.time()
        if detector.prev_palm_x and (current_time - last_swipe_time) > cooldown_time:
            if palm_x - detector.prev_palm_x > 50:  # Swipe left
                current_color = color_list.next_color()
                print("Swiped Left. Current Color:", current_color)
                calls.set_color(current_color[0], current_color[1], current_color[2])
                last_swipe_time = current_time

            elif detector.prev_palm_x - palm_x > 50:  # Swipe right
                current_color = color_list.prev_color()
                print("Swiped Right. Current Color:", current_color)
                calls.set_color(current_color[0], current_color[1], current_color[2])
                last_swipe_time = current_time

        detector.prev_palm_x = palm_x

    # cv2.namedWindow("Image", cv2.WINDOW_NORMAL)  # Create a resizable window
    # cv2.resizeWindow("Image", 800, 600)  # Set initial window size
    # cv2.imshow("Image", img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
