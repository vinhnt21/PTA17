from PyQt6 import uic
from PyQt6.QtWidgets import *


class Buoi7(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi7.ui", self)

        self.pushButton_2.clicked.connect(self.xu_ly_dang_ki)

    def xu_ly_dang_ki(self):
        tendangnhap = self.lineEdit.text()
        matkhau = self.lineEdit_2.text()
        matkhauxacnhan = self.lineEdit_3.text()

        if matkhau != matkhauxacnhan:
            QMessageBox.critical(self, "Lỗi", "Mật khẩu không khớp")
            return

        QMessageBox.information(self, "Thông báo", f"Đăng kí thành công\nTên đăng nhập: {tendangnhap}\nMật khẩu: {matkhau}")

app = QApplication([])
window = Buoi7()
window.show()
app.exec()
