import cv2
import os

path = "D:\Company\ZHuyQuang\Video\veh06.mp4"
path = os.path.join(os.path.abspath(path), "")
print(path)
cap = cv2.VideoCapture(path)

while True:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture(path)
        continue
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
