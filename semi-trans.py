# Write your code here :-)
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
alpha = 0.8

while True:
    _, img = cap.read()
    overlay = img.copy()
    output = img.copy()

    cv2.rectangle(overlay, (0,0), (640,240), (0,0,0), -1)
    cv2.addWeighted(overlay, alpha, output, 1- alpha, 0, output)
    cv2.imshow("Image", output)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
