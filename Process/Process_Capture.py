from PyQt5 import QtCore
import time
import sys
import numpy as np
import cv2


class CaptureThread(QtCore.QThread):

    def __init__(self, queue_capture, source):
        super().__init__()
        self.queue_capture = queue_capture
        self.source = source
        self.__thread_active = False

    def run(self):
        self.__thread_active = True
        print('Starting Capture Thread...')
        self.cap = cv2.VideoCapture(self.source)
        while self.__thread_active:
            ret, frame = self.cap.read()
            if not ret:
                print('Capture Thread: No frame')
                self.cap = cv2.VideoCapture(self.source)
                time.sleep(3)
                continue
            if self.queue_capture.qsize() < 1 and frame is not None:
                self.queue_capture.put(frame)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')

        self.__thread_active = False

        self.cap.release()
