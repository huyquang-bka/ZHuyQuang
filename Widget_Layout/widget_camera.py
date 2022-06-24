# -*- coding: utf-8 -*-

# self implementation generated from reading ui file '.\widget_camera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from Process.Process_Capture import CaptureThread
from queue import Queue


class Ui_Camera(QtWidgets.QWidget):

    def __init__(self, id, source):
        super().__init__()
        self.setupUi()
        self.id = id
        self.source = source
        # queue
        self.queue_capture = Queue()

        # thread
        self.thread_capture = CaptureThread(self.queue_capture, self.source)

        # start thread
        self.start_all_thread()

    def start_all_thread(self):
        self.thread_capture.start()

    def show_frame(self, frame_camera, current_frame):
        if current_frame is not None:
            rgb_img = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
            qt_img = QtGui.QPixmap.fromImage(
                QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
                frame_camera.width(), frame_camera.height())
            frame_camera.setPixmap(qt_img)
            frame_camera.setScaledContents(True)

    def paintEvent(self, event):
        if self.queue_capture.qsize() > 0:
            current_frame = self.queue_capture.get()
            self.show_frame(self.qlabel_camera, current_frame)
        self.update()

    def setupUi(self):
        self.setObjectName("Camera")
        self.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.qlabel_camera = QtWidgets.QLabel(self)
        self.qlabel_camera.setStyleSheet("background: beige")
        self.qlabel_camera.setObjectName("qlabel_camera")
        self.gridLayout.addWidget(self.qlabel_camera, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Camera", "Camera"))
        self.qlabel_camera.setText(_translate("Camera", "qlabel_camera"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    source = r"D:\ZHuyQuang\Video\a.mp4"
    ui = Ui_Camera(source)
    ui.show()
    sys.exit(app.exec_())
