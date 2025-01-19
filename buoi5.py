from PyQt6 import uic
from PyQt6.QtWidgets import *


class Buoi5(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi5.ui", self)


app = QApplication([])
window = Buoi5()
window.show()
app.exec()

