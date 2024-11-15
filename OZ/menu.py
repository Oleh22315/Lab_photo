# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThreadPool, QRunnable, Signal, QMutex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QWidget, QFileDialog)

import numpy as np
import time
import dask.array as da
from PIL import Image
from result import ResultWindow

class ImageProcessorSignals(QObject):
    finished = Signal(QImage)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1049, 636)
        MainWindow.setStyleSheet(u"background-color: rgb(52, 52, 52);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 511, 551))
        self.groupBox.setStyleSheet(u"border: 2px solid white; \n"
"border-radius: 5px;")
        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(270, 430, 221, 22))
        self.horizontalSlider.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(485, 452, 17, 15))
        self.label.setStyleSheet(u"border-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 452, 27, 15))
        self.label_2.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 490, 471, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: 2px solid rgb(176, 176, 176); \n"
"\n"
"")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 50, 471, 371))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(128, 428, 141, 21))
        self.label_7.setStyleSheet(u"border-color: rgb(52, 52, 52);\n"
"color: rgb(85, 170, 0);")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 481, 31))
        self.label_9.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 452, 181, 31))
        self.label_11.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(530, 10, 511, 551))
        self.groupBox_2.setStyleSheet(u"border: 2px solid white; \n"
"border-radius: 5px;")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 450, 27, 15))
        self.label_4.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(484, 450, 17, 15))
        self.label_3.setStyleSheet(u"border-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);")
        self.horizontalSlider_2 = QSlider(self.groupBox_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(270, 430, 221, 22))
        self.horizontalSlider_2.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 50, 471, 371))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(128, 428, 141, 21))
        self.label_8.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 10, 481, 31))
        self.label_10.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(120, 457, 179, 21))
        self.label_12.setStyleSheet(u"border-color: rgb(52, 52, 52);")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 490, 471, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: 2px solid rgb(176, 176, 176); ")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 580, 501, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border: 2px solid rgb(176, 176, 176); \n"
"border-radius: 5px;")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(540, 580, 491, 31))
        self.progressBar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #ffffff;
                border-radius: 5px;
                text-align: center;
                color: white;
            }

            QProgressBar::chunk {
                background-color: #7d7d7d;
                width: 20px;
            }
        """)
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    ################## Параметри ####################

        self.horizontalSlider.setMinimum(0)  
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)
        self.label_2.setText(f"{50}")
        self.label_2.setStyleSheet("color: rgb(255, 255, 255); border-color: rgb(52, 52, 52);")
        
        self.horizontalSlider_2.setMinimum(0)  
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setValue(50)
        self.label_4.setText(f"{50}")
        self.label_4.setStyleSheet("color: rgb(255, 255, 255); border-color: rgb(52, 52, 52);")

        self.progressBar.setVisible(False)
        self.pushButton.setVisible(False)

    ################## СИГНАЛИ ######################

        self.horizontalSlider.valueChanged.connect(self.updateSlider2)
        self.horizontalSlider_2.valueChanged.connect(self.updateSlider1)
        self.pushButton_2.clicked.connect(self.open_photo1)
        self.pushButton_3.clicked.connect(self.open_photo2)
        self.pushButton.clicked.connect(self.renderphoto)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0444\u043e\u0442\u043e", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">\u041a\u043e\u0435\u0444\u0456\u0446\u0456\u0454\u043d\u0442 \u043f\u0440\u043e\u0437\u043e\u0440\u043e\u0441\u0442\u0456:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">\u0424\u043e\u0442\u043e 1</span></p></body></html>", None))
        self.groupBox_2.setTitle("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">\u041a\u043e\u0435\u0444\u0456\u0446\u0456\u0454\u043d\u0442 \u043f\u0440\u043e\u0437\u043e\u0440\u043e\u0441\u0442\u0456:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">\u0424\u043e\u0442\u043e 2</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 \u0444\u043e\u0442\u043e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f", None))
    # retranslateUi

    def updateSlider2(self, value):

        newValue = 100 - value 
        self.horizontalSlider_2.setValue(max(newValue, 0))

        self.label_2.setText(f"{value}")
        self.label_2.setStyleSheet("color: rgb(255, 255, 255); border-color: rgb(52, 52, 52);")
        self.label_4.setText(f"{newValue}")
        self.label_4.setStyleSheet("color: rgb(255, 255, 255); border-color: rgb(52, 52, 52);")

    def updateSlider1(self, value):

        newValue = 100 - value 
        self.horizontalSlider.setValue(max(newValue, 0))

        self.label_2.setText(f"{newValue}")
        self.label_2.setStyleSheet("color: rgb(255, 255, 255); border-color: rgb(52, 52, 52);")
        self.label_4.setText(f"{value}")
        self.label_4.setStyleSheet("color: rgb(255, 255, 255); border-color: rgb(52, 52, 52);")

    image_1_path = ''
    image_2_path = ''
    
    def open_photo1(self, value):

        image_path, _ = QFileDialog.getOpenFileName(self, "Виберіть зображення", "", "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)")

        if image_path:
            self.image_1_path = image_path
            pixmap = QPixmap(image_path)  
            self.label_5.setPixmap(pixmap.scaled(self.label_5.size(), Qt.KeepAspectRatio))

    def open_photo2(self, value):

        image_path, _ = QFileDialog.getOpenFileName(self, "Виберіть зображення", "", "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)")

        if image_path:
            self.image_2_path = image_path
            pixmap = QPixmap(image_path)  
            self.label_6.setPixmap(pixmap.scaled(self.label_5.size(), Qt.KeepAspectRatio))

        self.pushButton.setVisible(True)

    def renderphoto(self):
        self.thread_pool = QThreadPool()
        alpha = self.horizontalSlider.value() / 100.0
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)

        start_time = time.time()
        self.blend_images(self.image_1_path, self.image_2_path, alpha)
        end_time = time.time()

        print(str(end_time-start_time))

    def blend_images(self, image1_path, image2_path, alpha):
        image1_rgb = Image.open(image1_path).convert("RGBA")
        image2_rgb = Image.open(image2_path).convert("RGBA")

        if image1_rgb.size != image2_rgb.size:
            image2_rgb = image2_rgb.resize(image1_rgb.size, Image.LANCZOS)

        image1 = np.array(image1_rgb, dtype=np.float32)
        image2 = np.array(image2_rgb, dtype=np.float32)

        result_image = np.zeros_like(image1, dtype=np.uint8)

        num_threads = 4
        rows_per_thread = image1.shape[0] // num_threads

        mutex = QMutex()

        progress_step = 100 / num_threads

        for i in range(num_threads):
            start_row = i * rows_per_thread
            end_row = (i + 1) * rows_per_thread if i < num_threads - 1 else image1.shape[0]

            image1_block = image1[start_row:end_row, :, :]
            image2_block = image2[start_row:end_row, :, :]
            result_block = result_image

            blended_block = (alpha * image1_block + (1 - alpha) * image2_block).astype(np.uint8)

            mutex.lock()
            result_block[start_row:end_row, :, :] = blended_block
            mutex.unlock()

            progress_value = int((i + 1) * progress_step)
            self.progressBar.setValue(progress_value)

        blended_qimage = QImage(result_image.data, result_image.shape[1], result_image.shape[0], QImage.Format_RGBA8888)
        self.display_result(blended_qimage)
        self.progressBar.setValue(100)

    def display_result(self, result_image):
        pixmap = QPixmap.fromImage(result_image)

        self.second_window = ResultWindow(pixmap)
        self.second_window.show()




    


