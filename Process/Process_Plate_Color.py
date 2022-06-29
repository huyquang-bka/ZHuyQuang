from PyQt5 import QtCore
import time
import cv2
import numpy as np


class ThreadPlateColor(QtCore.QThread):

    def __init__(self, queue_plate, queue_plate_color):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_plate = queue_plate
        self.queue_plate_color = queue_plate_color

        self.middle_height = 400

        # hsv
        self.lower_yellow = np.array([20, 50, 50])
        self.upper_yellow = np.array([40, 255, 255])

        self.lower_blue = np.array([100, 50, 50])
        self.upper_blue = np.array([140, 255, 255])

        self.lower_red = np.array([0, 50, 50])
        self.upper_red = np.array([10, 255, 255])

    def most_frequent(self, ls):
        try:
            return max(set(ls), key=ls.count)
        except:
            return ""

    def detect_color(self, image):
        H, W = image.shape[:2]
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # lower_dark_blue = np.array([100, 100, 100])
        # upper_dark_blue = np.array([140, 255, 255])

        mask_yellow = cv2.inRange(hsv, self.lower_yellow, self.upper_yellow)
        mask_blue = cv2.inRange(hsv, self.lower_blue, self.upper_blue)
        mask_red = cv2.inRange(hsv, self.lower_red, self.upper_red)

        count_yellow = cv2.countNonZero(mask_yellow)
        count_blue = cv2.countNonZero(mask_blue)
        count_red = cv2.countNonZero(mask_red)

        if count_yellow > H * W * 0.3:
            return "yellow"
        elif count_blue > H * W * 0.3:
            return "blue"
        elif count_red > H * W * 0.3:
            return "red"
        else:
            return "white"

    def run(self):
        self.__thread_active = True
        print('Starting Plate Color Thread...')
        count = 0
        plate_color_dict = {}
        while self.__thread_active:
            if self.queue_plate.qsize() > 0:
                print('Plate Color Thread: Processing...')
                frame, id_dict = self.queue_plate.get()
                result_dict = {}
                for id, bbox in id_dict.items():
                    count += 1
                    box, plate_box = bbox
                    x1, y1, x2, y2 = box
                    if not plate_box:
                        if (y1 + y2) // 2 > self.middle_height:
                            list_key = list(plate_color_dict.keys())
                            if id in list_key:
                                plate_color_dict[id].append(" ")
                                lp_text = self.most_frequent(plate_color_dict[id])
                                result_dict[id] = lp_text
                                del plate_color_dict[id]
                            if self.queue_plate_color.qsize() < 1 and result_dict:
                                # print("Digit: ", plate_color_dict)
                                self.queue_plate_color.put(result_dict)
                        continue

                    try:
                        plate_color_dict[id]
                    except:
                        plate_color_dict[id] = []

                    x1_, y1_, x2_, y2_, cls_, conf_ = plate_box
                    crop = frame[y1:y2, x1:x2]
                    lp_crop = crop[y1_:y2_, x1_:x2_]
                    plate_color = self.detect_color(lp_crop)
                    print(plate_color)
                    plate_color_dict[id].append(plate_color)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Plate Color Thread')
        self.__thread_active = False
