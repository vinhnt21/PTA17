from PyQt6 import uic
from PyQt6.QtWidgets import *


class Dangki(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi8_dangki.ui", self)

        self.pushButton.clicked.connect(self.show_dangnhap)

    def show_dangnhap(self):
        dangki.hide()
        dangnhap.show()


class Dangnhap(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi8_dangnhap.ui", self)

        self.pushButton.clicked.connect(self.show_dangki)
        self.pushButton_2.clicked.connect(self.login)

    def show_dangki(self):
        dangnhap.hide()
        dangki.show()

    def login(self):
        tendangnhap = self.lineEdit.text()
        matkhau = self.lineEdit_2.text()

        if not tendangnhap or not matkhau:
            QMessageBox.critical(self, "Lỗi", "Chưa nhập tên đăng nhập hoặc mật khẩu")
            return

        if tendangnhap == "admin" and matkhau == "admin":
            main.show()
            dangnhap.hide()
        else:
            QMessageBox.critical(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu")


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi8_main.ui", self)


app = QApplication([])

dangki = Dangki()
dangnhap = Dangnhap()
main = Main()


dangnhap.show()

app.exec()
