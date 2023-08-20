# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets 


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 139)
        self.text = QtWidgets.QLabel(Dialog)
        self.text.setGeometry(QtCore.QRect(80, 40, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text.setObjectName("text")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 90, 411, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_recent = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.open_recent.setFont(font)
        self.open_recent.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.open_recent)
        self.new_dox = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.new_dox.setFont(font)
        self.new_dox.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.new_dox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.text.setText(_translate("Dialog", "هل تريد انشاء ملف جديد او فتح مستند موجود مسبقا ؟"))
        self.open_recent.setText(_translate("Dialog", "فتح مستند سابق"))
        self.new_dox.setText(_translate("Dialog", "انشاء جديد"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
