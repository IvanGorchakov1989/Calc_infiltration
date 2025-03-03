# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'form.ui'
#
# Created by: Qt User Interface Compiler version 6.7.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QIcon, QPixmap)
from PySide6.QtWidgets import (QAbstractScrollArea, QComboBox, QFrame,
                               QGroupBox, QLabel, QLineEdit,
                               QMenuBar, QPushButton, QSizePolicy, QTextBrowser,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(640, 650))
        MainWindow.setMaximumSize(QSize(640, 650))
        icon = QIcon()
        icon.addFile(u"src/Icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 640, 640))
        self.groupBox.setFlat(False)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 620, 180))
        self.label.setPixmap(QPixmap(u"src/1.png"))
        self.label.setScaledContents(True)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 300, 620, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(5, 0, 60, 30))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(65, 0, 240, 30))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(375, 0, 50, 30))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(315, 0, 50, 30))
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 220, 620, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(365, 0, 100, 30))
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(10)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(5, 0, 360, 30))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 340, 620, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(5, 0, 60, 30))
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(65, 0, 240, 30))
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(375, 0, 70, 30))
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 1, 60, 28))
        self.lineEdit.setFrame(True)
        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 380, 620, 90))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(5, 30, 60, 30))
        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(375, 30, 50, 30))
        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(315, 30, 50, 30))
        self.textBrowser = QTextBrowser(self.frame_4)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(65, 2, 240, 86))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setFocusPolicy(Qt.NoFocus)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textBrowser.setOpenLinks(False)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(510, 480, 120, 30))
        icon1 = QIcon()
        iconThemeName = u"emblem-default"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.pushButton.setIcon(icon1)
        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 260, 620, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.comboBox_2 = QComboBox(self.frame_5)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(0, 0, 340, 30))
        self.comboBox_2.setEditable(False)
        self.comboBox_3 = QComboBox(self.frame_5)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(345, 0, 275, 30))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setMaxVisibleItems(10)
        self.textBrowser_2 = QTextBrowser(self.groupBox)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(10, 520, 620, 90))
        self.textBrowser_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textBrowser_2.setOpenLinks(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 29))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u043e\u0442\u043e\u043f\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u041f 131.13330.2020 \u0421\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043a\u043b\u0438\u043c\u0430\u0442\u043e\u043b\u043e\u0433\u0438\u044f", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"T\u043d =>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u043b\u043e\u0434\u043d\u0430\u044f \u043f\u044f\u0442\u0438\u0434\u043d\u0435\u0432\u043a\u0430 =", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"t* C", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0432\u043e\u0437\u0434\u0443\u0445\u0430 \u0432 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0438:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"L =>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434 \u0432\u043e\u0437\u0434\u0443\u0445\u0430 =", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u043c3/\u0447\u0430\u0441", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Q =>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0412\u0442", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0418\u043d\u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u043e\u0442\u043e\u043f\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0436\u0438\u043b\u044b\u0445 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u0439 =</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.comboBox_2.setCurrentText("")
        self.comboBox_3.setCurrentText("")
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u0433\u043e\u0440\u043e\u0434\u043e\u0432, \u043e\u0442\u043c\u0435\u0447\u0435\u043d\u043d\u044b\u0445 \u00ab*\u00bb, \u0443\u043a\u0430\u0437\u0430\u043d\u0430 \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0432\u043e\u0437\u0434\u0443\u0445\u0430 \u043d\u0430\u0438\u0431\u043e\u043b\u0435\u0435 \u0445\u043e\u043b\u043e\u0434\u043d\u043e\u0439 \u043f\u044f\u0442"
                        "\u0438\u0434\u043d\u0435\u0432\u043a\u0438, \u00b0\u0421, \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u043d\u043e\u0441\u0442\u044c\u044e 0,98</p></body></html>", None))
    # retranslateUi
