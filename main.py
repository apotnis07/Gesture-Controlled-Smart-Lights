import cv2
import HandTrackingModule as htm
import api_calls as api
import time

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
calls = api.API_Calls()
brightness = 100
last_request_time = time.time()  # Tracks the last API call
rate_limit_interval = 3  # Minimum time interval (seconds) between requests

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        num_fingers = sum(fingers1)
        new_brightness = num_fingers * 20  # Map fingers (1-5) to brightness (20-100)

        # Send API call only if brightness changes and rate-limit allows
        if new_brightness != brightness and (time.time() - last_request_time) > rate_limit_interval:
            brightness = new_brightness
            print(f"Setting Brightness: {brightness}")
            calls.set_brightness(brightness)
            last_request_time = time.time()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
