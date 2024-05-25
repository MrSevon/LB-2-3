from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5 import uic, QtWidgets, QtCore
from random import randint

import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(150, 240, 75, 23))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Задание 2"))
        self.btn.setText(_translate("Form", "Клик"))

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_UI()
        self.draw_check = False

    def init_UI(self):
        self.btn.clicked.connect(self.draw)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawClick(qp)
        qp.end()

    def drawClick(self, qp):
        color = QColor(244,169,0)
        qp.setPen(color)
        size = randint(2, 100)

        if self.draw_check:
            qp.drawEllipse(150, 80, size, size)
        
    def draw(self):
        self.draw_check = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()