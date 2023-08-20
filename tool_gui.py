# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from http.server import BaseHTTPRequestHandler, HTTPServer

from PyQt5.QtWidgets import QFileDialog
from document_dialog import Ui_Dialog
from utils import *
import sys

_word_app = None

# Define a custom subclass of BaseHTTPRequestHandler
class custom_http_server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        global _word_app
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Read the POST request data from the request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
                
        insert_image( _word_app , post_data)
        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

class Ui_MainWindow(object):
    def on_dialog_button_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(QtWidgets.QDialog(), "Open File", "", "All Files (*)", options=options)

        if file_name:
            print("Selected File:", file_name)
            MainWindow.showMinimized()
            self.dialog.accept()            
            return file_name

    def open_dialog(self):
        self.dialog = QtWidgets.QDialog()
        self.ui_dialog = Ui_Dialog()
        self.ui_dialog.setupUi(self.dialog)
        self.ui_dialog.new_dox.clicked.connect(self.on_wordButton_clicked)
        self.ui_dialog.open_recent.clicked.connect(self.on_dialog_button_clicked)
        self.dialog.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 136)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(369, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.wordButton = QtWidgets.QPushButton(self.centralwidget )
        self.wordButton.clicked.connect(self.open_dialog)
        self.wordButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wordButton.setFont(font)
        self.wordButton.setObjectName("wordButton")
        self.gridLayout.addWidget(self.wordButton, 0, 0, 1, 1)
        self.checkImagesButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkImagesButton.setFont(font)
        self.checkImagesButton.setObjectName("checkImagesButton")
        self.gridLayout.addWidget(self.checkImagesButton, 2, 0, 1, 1)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        self.gridLayout.addWidget(self.convertButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "اداة المعادلات"))
        self.wordButton.setText(_translate("MainWindow", "فتح تطبيق ورد"))
        self.checkImagesButton.setText(_translate("MainWindow", "التحقق من صور المعادلات"))
        self.convertButton.setText(_translate("MainWindow", "تحويل صور المعادلات الى لاتيك"))
        
    def on_wordButton_clicked(self):
        global _word_app        # FIXME: غير هذا الاسلوب و استخدم البرمجة الشيئية بدل من تعريف المتغير كمتغير عالمي
        self.dialog.accept()
        MainWindow.showMinimized()
        _word_app = open_word()
        create_new_document(_word_app)
        self.start_server()

    def on_convertButton_clicked(self):
        # Code to be executed when the second push button is clicked
        print("Converting equations images to LaTeX...")
    
    def start_server(self):
        # Start the HTTP server
        with HTTPServer(('', 8000), custom_http_server) as server:
            server.serve_forever()

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("successful exit")