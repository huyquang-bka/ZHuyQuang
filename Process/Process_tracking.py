from PyQt5 import QtCore
import time
import cv2
from Yolov5.detect_yolov5 import Tracking


class CaptureThread(QtCore.QThread):

    def __init__(self, queue_capture, queue_tracking):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_capture = queue_capture
        self.queue_tracking = queue_tracking

        # tracking
        self.tracking = Tracking()
        self.setup_tracking()

    def setup_tracking(self):
        weights = "Weight/yolov5s.pt"
        classes = [2, 7]
        conf = 0.3
        imgsz = 640
        device = "0"
        self.tracking.setup_model(weights, classes, conf, imgsz, device)

    def run(self):
        self.__thread_active = True
        print('Starting Tracking Thread...')
        while self.__thread_active:
            if self.queue_capture.qsize() > 0:
                frame = self.queue_capture.get()
                id_dict = self.tracking.detect(frame)
                if self.queue_tracking.qsize() < 1:
                    self.queue_tracking.put(id_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
        self.cap.release()
