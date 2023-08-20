# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\programming\MathImage2Word\tool_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 177)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(369, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wordButton = QtWidgets.QPushButton(self.centralwidget)
        self.wordButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wordButton.setFont(font)
        self.wordButton.setObjectName("wordButton")
        self.verticalLayout.addWidget(self.wordButton)
        self.checkImagesButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkImagesButton.setFont(font)
        self.checkImagesButton.setObjectName("checkImagesButton")
        self.verticalLayout.addWidget(self.checkImagesButton)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        self.verticalLayout.addWidget(self.convertButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.address = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.address.setFont(font)
        self.address.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.address.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.address.setText("")
        self.address.setAlignment(QtCore.Qt.AlignCenter)
        self.address.setObjectName("address")
        self.horizontalLayout.addWidget(self.address)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "اداة المعادلات"))
        self.wordButton.setText(_translate("MainWindow", "فتح تطبيق ورد"))
        self.checkImagesButton.setText(_translate("MainWindow", "التحقق من صور المعادلات"))
        self.convertButton.setText(_translate("MainWindow", "تحويل صور المعادلات الى لاتيك"))
        self.label.setText(_translate("MainWindow", "عنوان الجهاز الداخلي "))
