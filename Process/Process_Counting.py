from PyQt5 import QtCore
from Polygon.Polygon import detect_polygon
import cv2


class ThreadCounting(QtCore.QThread):
    sig_count_motor = QtCore.pyqtSignal(int)
    sig_count_car = QtCore.pyqtSignal(int)

    def __init__(self, queue_tracking_for_count):
        super().__init__()
        self.__thread_active = False

        # queue
        self.queue_tracking_for_count = queue_tracking_for_count

    def is_in_detect_zone(self, box):
        x1, y1, x2, y2 = box
        return cv2.pointPolygonTest(detect_polygon, ((x1 + x2) // 2, y2), False) > 0

    def run(self):
        self.__thread_active = True
        print('Starting Tracking Thread...')
        list_id = []
        while self.__thread_active:
            if self.queue_tracking_for_count.qsize() > 0:
                frame, tracking_dict = self.queue_tracking_for_count.get()
                for id, value in tracking_dict.items():
                    if id in list_id:
                        continue
                    x1, y1, x2, y2, category = value[:5]
                    if not self.is_in_detect_zone([x1, y1, x2, y2]):
                        continue
                    if int(category) == 3:
                        self.sig_count_motor.emit(0)
                    else:
                        self.sig_count_car.emit(0)
                    list_id.append(id)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Capture Thread')
        self.__thread_active = False
