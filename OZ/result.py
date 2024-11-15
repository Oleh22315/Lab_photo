# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Result.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,Qt)
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QFileDialog

class ResultWindow(QWidget):
    def __init__(self,pix):
        super().__init__()
        self.setFixedSize(570, 575)
        self.setStyleSheet(u"background-color: rgb(52, 52, 52);")
        
        
        self.centralwidget = QWidget(self)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 551, 431))
        self.label.setStyleSheet(u"border: 2px solid white; \n"
                                 "border-radius: 5px;")
        
        self.label.setPixmap(pix.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 561, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 510, 191, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                      "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                      "border: 2px solid rgb(176, 176, 176); \n"
                                      "border-radius: 5px;")
        
        self.pushButton.clicked.connect(self.download)
        
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("ResultWindow", u"Result", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("ResultWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">\u0417\u0433\u0435\u043d\u0435\u0440\u043e\u0432\u0430\u043d\u0435 \u0444\u043e\u0442\u043e</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("ResultWindow", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0444\u043e\u0442\u043e", None))

    def download(self):

        pixmap = self.label.pixmap()
        
        file_path, _ = QFileDialog.getSaveFileName(self, "Зберегти зображення", "", "PNG Files (*.png);;JPEG Files (*.jpg);;BMP Files (*.bmp);;TIFF Files (*.tiff);;GIF Files (*.gif)")
        if file_path:
                
            pixmap.save(file_path)

        self.close()
        



