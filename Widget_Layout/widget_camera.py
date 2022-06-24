# -*- coding: utf-8 -*-

# self implementation generated from reading ui file '.\widget_camera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from Process.Process_Capture import CaptureThread
from Widget_Layout.widget_camera_setup import Widget_Camera_Item
from queue import Queue


class Ui_Camera(Widget_Camera_Item):

    def __init__(self):
        super().__init__()
        # queue
        self.queue_output = Queue()
        self.queue_capture = Queue()

    def setup(self, id, source):
        self.id = id
        self.source = source

    def create_thread(self):
        self.thread_capture = CaptureThread(self.queue_capture, self.source)

    def start_all_thread(self):
        self.group_settings.hide()
        self.camera_frame.show()
        self.thread_capture.start()

    def stop_all_thread(self):
        self.thread_capture.stop()
        self.camera_frame.clear()
        self.camera_frame.hide()
        self.group_settings.show()

    def paintEvent(self, event):
        if self.queue_output.qsize() > 0:
            current_frame = self.queue_output.get()
            self.show_frame(self.camera_frame, current_frame)
        self.update()

    def show_frame(self, frame_camera, current_frame):
        if current_frame is not None:
            rgb_img = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
            qt_img = QtGui.QPixmap.fromImage(
                QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
                frame_camera.width(), frame_camera.height())
            frame_camera.setPixmap(qt_img)
            frame_camera.setScaledContents(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    source = r"D:\ZHuyQuang\Video\a.mp4"
    ui = Ui_Camera("1", source)
    ui.show()
    sys.exit(app.exec_())
