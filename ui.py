# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(799, 607)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_source = QtGui.QLabel(self.centralwidget)
        self.label_source.setGeometry(QtCore.QRect(10, 10, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_source.setFont(font)
        self.label_source.setObjectName(_fromUtf8("label_source"))
        self.group_left = QtGui.QGroupBox(self.centralwidget)
        self.group_left.setEnabled(True)
        self.group_left.setGeometry(QtCore.QRect(10, 30, 261, 541))
        self.group_left.setTitle(_fromUtf8(""))
        self.group_left.setObjectName(_fromUtf8("group_left"))
        self.list = QtGui.QListWidget(self.group_left)
        self.list.setGeometry(QtCore.QRect(0, 0, 261, 491))
        self.list.setObjectName(_fromUtf8("list"))
        self.btn_addMore = QtGui.QPushButton(self.group_left)
        self.btn_addMore.setGeometry(QtCore.QRect(100, 500, 151, 29))
        self.btn_addMore.setObjectName(_fromUtf8("btn_addMore"))
        self.btn_moveDown = QtGui.QPushButton(self.group_left)
        self.btn_moveDown.setGeometry(QtCore.QRect(40, 500, 31, 31))
        self.btn_moveDown.setObjectName(_fromUtf8("btn_moveDown"))
        self.btn_moveUp = QtGui.QPushButton(self.group_left)
        self.btn_moveUp.setGeometry(QtCore.QRect(10, 500, 31, 31))
        self.btn_moveUp.setObjectName(_fromUtf8("btn_moveUp"))
        self.group_right = QtGui.QGroupBox(self.centralwidget)
        self.group_right.setGeometry(QtCore.QRect(280, 10, 512, 561))
        self.group_right.setTitle(_fromUtf8(""))
        self.group_right.setObjectName(_fromUtf8("group_right"))
        self.img_preview = QtGui.QLabel(self.group_right)
        self.img_preview.setGeometry(QtCore.QRect(0, 0, 512, 512))
        self.img_preview.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.img_preview.setAutoFillBackground(False)
        self.img_preview.setText(_fromUtf8(""))
        self.img_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.img_preview.setObjectName(_fromUtf8("img_preview"))
        self.toggle_loop = QtGui.QCheckBox(self.group_right)
        self.toggle_loop.setGeometry(QtCore.QRect(80, 520, 61, 22))
        self.toggle_loop.setChecked(False)
        self.toggle_loop.setObjectName(_fromUtf8("toggle_loop"))
        self.btn_scaleUp = QtGui.QPushButton(self.group_right)
        self.btn_scaleUp.setGeometry(QtCore.QRect(140, 520, 21, 21))
        self.btn_scaleUp.setObjectName(_fromUtf8("btn_scaleUp"))
        self.btn_scaleDown = QtGui.QPushButton(self.group_right)
        self.btn_scaleDown.setGeometry(QtCore.QRect(160, 520, 21, 21))
        self.btn_scaleDown.setObjectName(_fromUtf8("btn_scaleDown"))
        self.btn_save = QtGui.QPushButton(self.group_right)
        self.btn_save.setGeometry(QtCore.QRect(350, 520, 151, 31))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.text_fps = QtGui.QTextEdit(self.group_right)
        self.text_fps.setEnabled(True)
        self.text_fps.setGeometry(QtCore.QRect(0, 520, 51, 21))
        self.text_fps.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_fps.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.text_fps.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_fps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_fps.setAutoFormatting(QtGui.QTextEdit.AutoNone)
        self.text_fps.setDocumentTitle(_fromUtf8(""))
        self.text_fps.setObjectName(_fromUtf8("text_fps"))
        self.label = QtGui.QLabel(self.group_right)
        self.label.setGeometry(QtCore.QRect(50, 520, 21, 17))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpen = QtGui.QMenu(self.menubar)
        self.menuOpen.setObjectName(_fromUtf8("menuOpen"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_gif = QtGui.QAction(MainWindow)
        self.actionOpen_gif.setObjectName(_fromUtf8("actionOpen_gif"))
        self.actionOpen_folder_with_PNGs = QtGui.QAction(MainWindow)
        self.actionOpen_folder_with_PNGs.setObjectName(_fromUtf8("actionOpen_folder_with_PNGs"))
        self.menuOpen.addAction(self.actionOpen_gif)
        self.menuOpen.addAction(self.actionOpen_folder_with_PNGs)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "stripmaker2.0", None))
        self.label_source.setText(_translate("MainWindow", "select source first", None))
        self.btn_addMore.setText(_translate("MainWindow", "add more PNGs", None))
        self.btn_moveDown.setText(_translate("MainWindow", "↓", None))
        self.btn_moveUp.setText(_translate("MainWindow", "↑", None))
        self.toggle_loop.setText(_translate("MainWindow", "loop", None))
        self.btn_scaleUp.setText(_translate("MainWindow", "+", None))
        self.btn_scaleDown.setText(_translate("MainWindow", "-", None))
        self.btn_save.setText(_translate("MainWindow", "save strip as", None))
        self.text_fps.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">60</p></body></html>", None))
        self.label.setText(_translate("MainWindow", "fps", None))
        self.menuOpen.setTitle(_translate("MainWindow", "open", None))
        self.actionOpen_gif.setText(_translate("MainWindow", "open GIF", None))
        self.actionOpen_folder_with_PNGs.setText(_translate("MainWindow", "open folder with PNGs", None))
