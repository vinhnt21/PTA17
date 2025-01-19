from PyQt6 import uic
from PyQt6.QtWidgets import *


class Buoi6(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi6.ui", self)


app = QApplication([])
window = Buoi6()
window.show()
app.exec()
