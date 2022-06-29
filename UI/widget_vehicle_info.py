# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\vehicle_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(540, 562)
        widget.setWindowTitle("")
        widget.setStyleSheet("background-color: rgb(250, 255, 238);")
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setStyleSheet("background-color: rgb(243, 255, 254);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qlabel_registration = QtWidgets.QLabel(self.groupBox)
        self.qlabel_registration.setStyleSheet("\n"
"background-color: rgb(0, 213, 0);")
        self.qlabel_registration.setText("")
        self.qlabel_registration.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_registration.setObjectName("qlabel_registration")
        self.gridLayout_2.addWidget(self.qlabel_registration, 6, 0, 1, 1)
        self.qlabel_date_registration = QtWidgets.QLabel(self.groupBox)
        self.qlabel_date_registration.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_date_registration.setStyleSheet("background-color: rgb(132, 231, 228);")
        self.qlabel_date_registration.setText("")
        self.qlabel_date_registration.setObjectName("qlabel_date_registration")
        self.gridLayout_2.addWidget(self.qlabel_date_registration, 11, 1, 1, 1)
        self.qlabel_time = QtWidgets.QLabel(self.groupBox)
        self.qlabel_time.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_time.setStyleSheet("background-color: rgb(203, 247, 255);")
        self.qlabel_time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.qlabel_time.setObjectName("qlabel_time")
        self.gridLayout_2.addWidget(self.qlabel_time, 1, 1, 1, 1)
        self.qlabel_brand = QtWidgets.QLabel(self.groupBox)
        self.qlabel_brand.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_brand.setStyleSheet("background-color: rgb(226, 249, 255);")
        self.qlabel_brand.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.qlabel_brand.setObjectName("qlabel_brand")
        self.gridLayout_2.addWidget(self.qlabel_brand, 2, 1, 1, 1)
        self.qlabel_plate = QtWidgets.QLabel(self.groupBox)
        self.qlabel_plate.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_plate.setStyleSheet("background-color: rgb(226, 249, 255);")
        self.qlabel_plate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.qlabel_plate.setObjectName("qlabel_plate")
        self.gridLayout_2.addWidget(self.qlabel_plate, 4, 1, 1, 1)
        self.qlabel_owner_res = QtWidgets.QLabel(self.groupBox)
        self.qlabel_owner_res.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_owner_res.setStyleSheet("background-color: rgb(171, 255, 253);")
        self.qlabel_owner_res.setText("")
        self.qlabel_owner_res.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.qlabel_owner_res.setObjectName("qlabel_owner_res")
        self.gridLayout_2.addWidget(self.qlabel_owner_res, 8, 1, 1, 1)
        self.qlabel_image_owner = QtWidgets.QLabel(self.groupBox)
        self.qlabel_image_owner.setStyleSheet("background: black")
        self.qlabel_image_owner.setObjectName("qlabel_image_owner")
        self.gridLayout_2.addWidget(self.qlabel_image_owner, 8, 0, 4, 1)
        self.qlabel_brand_res = QtWidgets.QLabel(self.groupBox)
        self.qlabel_brand_res.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_brand_res.setStyleSheet("background-color: rgb(132, 231, 228);")
        self.qlabel_brand_res.setText("")
        self.qlabel_brand_res.setObjectName("qlabel_brand_res")
        self.gridLayout_2.addWidget(self.qlabel_brand_res, 9, 1, 1, 1)
        self.qlabel_color_res = QtWidgets.QLabel(self.groupBox)
        self.qlabel_color_res.setStyleSheet("background-color: rgb(171, 255, 253);")
        self.qlabel_color_res.setText("")
        self.qlabel_color_res.setObjectName("qlabel_color_res")
        self.gridLayout_2.addWidget(self.qlabel_color_res, 10, 1, 1, 1)
        self.qlabel_web_api = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.qlabel_web_api.setFont(font)
        self.qlabel_web_api.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.qlabel_web_api.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_web_api.setObjectName("qlabel_web_api")
        self.gridLayout_2.addWidget(self.qlabel_web_api, 7, 0, 1, 2)
        self.qlabel_color = QtWidgets.QLabel(self.groupBox)
        self.qlabel_color.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_color.setStyleSheet("background-color: rgb(203, 247, 255);")
        self.qlabel_color.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.qlabel_color.setObjectName("qlabel_color")
        self.gridLayout_2.addWidget(self.qlabel_color, 3, 1, 1, 1)
        self.qlabel_speed = QtWidgets.QLabel(self.groupBox)
        self.qlabel_speed.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_speed.setStyleSheet("background-color: rgb(203, 247, 255);")
        self.qlabel_speed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.qlabel_speed.setObjectName("qlabel_speed")
        self.gridLayout_2.addWidget(self.qlabel_speed, 6, 1, 1, 1)
        self.qlabel_cam_id = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.qlabel_cam_id.setFont(font)
        self.qlabel_cam_id.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.qlabel_cam_id.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_cam_id.setObjectName("qlabel_cam_id")
        self.gridLayout_2.addWidget(self.qlabel_cam_id, 0, 0, 1, 2)
        self.qlabel_plate_type = QtWidgets.QLabel(self.groupBox)
        self.qlabel_plate_type.setMinimumSize(QtCore.QSize(0, 0))
        self.qlabel_plate_type.setStyleSheet("background-color: rgb(226, 249, 255);")
        self.qlabel_plate_type.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.qlabel_plate_type.setObjectName("qlabel_plate_type")
        self.gridLayout_2.addWidget(self.qlabel_plate_type, 5, 1, 1, 1)
        self.qlabel_image_car = QtWidgets.QLabel(self.groupBox)
        self.qlabel_image_car.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.qlabel_image_car.setStyleSheet("background: black")
        self.qlabel_image_car.setText("")
        self.qlabel_image_car.setObjectName("qlabel_image_car")
        self.gridLayout_2.addWidget(self.qlabel_image_car, 1, 0, 5, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        self.qlabel_time.setText(_translate("widget", "17-6-2022 09:22:30"))
        self.qlabel_brand.setText(_translate("widget", "Lamborghini"))
        self.qlabel_plate.setText(_translate("widget", "29A99999"))
        self.qlabel_image_owner.setText(_translate("widget", "TextLabel"))
        self.qlabel_web_api.setText(_translate("widget", "THÔNG TIN ĐĂNG KIỂM"))
        self.qlabel_color.setText(_translate("widget", "gold"))
        self.qlabel_speed.setText(_translate("widget", "100 km/h"))
        self.qlabel_cam_id.setText(_translate("widget", "camera 01"))
        self.qlabel_plate_type.setText(_translate("widget", "29A99999"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
