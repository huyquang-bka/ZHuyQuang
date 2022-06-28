from PyQt5 import QtCore
import time
import cv2


class ThreadShow(QtCore.QThread):

    def __init__(self, queue_tracking, queue_output):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking = queue_tracking
        self.queue_output = queue_output

        # signal
        self.summary_dict = {}

    def slot_summary(self, summary_dict):
        self.summary_dict = summary_dict
        print(self.summary_dict)

    def draw(self, frame, id_dict):
        for k, v in id_dict.items():
            x1, y1, x2, y2, category = v
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, str(k), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    def run(self):
        self.__thread_active = True
        print('Starting Tracking Thread...')
        while self.__thread_active:
            if self.queue_tracking.qsize() > 0:
                frame, id_dict = self.queue_tracking.get()
                self.draw(frame, id_dict)
                if self.queue_output.qsize() < 1:
                    self.queue_output.put(frame)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
