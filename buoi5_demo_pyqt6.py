import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt6.QtGui import QLinearGradient, QPalette, QColor, QBrush
from PyQt6.QtCore import Qt


class StudentManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý Học sinh")
        self.setGeometry(100, 100, 800, 600)

        # Thiết lập gradient cho toàn bộ ứng dụng
        self.setStyleSheet(
            """
            QMainWindow {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #FF6B6B,
                    stop: 0.3 #4ECDC4,
                    stop: 0.6 #45B7D1,
                    stop: 1 #96CEB4
                );
            }
            QWidget {
                font-family: Arial;
                font-size: 12px;
            }
            QLabel {
                color: white;
                font-weight: bold;
                font-size: 13px;
                padding: 5px;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #4ECDC4;
                border-radius: 10px;
                background: rgba(255, 255, 255, 0.9);
                color: #333;
            }
            QPushButton {
                padding: 10px 20px;
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #4ECDC4,
                    stop: 1 #45B7D1
                );
                border: none;
                border-radius: 15px;
                color: white;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #45B7D1,
                    stop: 1 #4ECDC4
                );
            }
            QTableWidget {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                padding: 5px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #4ECDC4;
                color: white;
            }
            QHeaderView::section {
                background-color: #45B7D1;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
        """
        )

        # Khởi tạo danh sách học sinh
        self.students = []

        # Tạo widget chính
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Form nhập liệu
        form_layout = QHBoxLayout()

        # Tạo các trường nhập liệu
        self.id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.class_input = QLineEdit()

        # Layout cho form
        form_widget = QWidget()
        form_layout = QVBoxLayout(form_widget)

        # Thêm padding cho form
        form_widget.setContentsMargins(20, 20, 20, 20)

        # Container cho form với background màu bán trong suốt
        form_container = QWidget()
        form_container.setStyleSheet(
            """
            QWidget {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 20px;
            }
        """
        )
        form_container_layout = QVBoxLayout(form_container)

        # Thêm các label và input
        form_layout.addWidget(QLabel("Mã học sinh:"))
        form_layout.addWidget(self.id_input)
        form_layout.addWidget(QLabel("Họ và tên:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Tuổi:"))
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(QLabel("Lớp:"))
        form_layout.addWidget(self.class_input)

        # Nút chức năng
        button_layout = QHBoxLayout()
        add_button = QPushButton("Thêm")
        update_button = QPushButton("Cập nhật")
        delete_button = QPushButton("Xóa")
        clear_button = QPushButton("Xóa form")

        button_layout.addWidget(add_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(clear_button)
        form_layout.addLayout(button_layout)

        # Thêm form layout vào container
        form_container_layout.addLayout(form_layout)

        # Tạo bảng hiển thị
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["Mã học sinh", "Họ và tên", "Tuổi", "Lớp"]
        )

        # Chỉnh style cho bảng
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setShowGrid(True)

        # Thêm các widget vào layout chính
        layout.addWidget(form_container)
        layout.addWidget(self.table)

        # Kết nối các sự kiện
        add_button.clicked.connect(self.add_student)
        update_button.clicked.connect(self.update_student)
        delete_button.clicked.connect(self.delete_student)
        clear_button.clicked.connect(self.clear_form)
        self.table.itemClicked.connect(self.load_student)

        # Cập nhật bảng
        self.update_table()

    def add_student(self):
        student_id = self.id_input.text()
        name = self.name_input.text()
        age = self.age_input.text()
        class_name = self.class_input.text()

        if not all([student_id, name, age, class_name]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        if any(s["id"] == student_id for s in self.students):
            QMessageBox.warning(self, "Lỗi", "Mã học sinh đã tồn tại!")
            return

        self.students.append(
            {"id": student_id, "name": name, "age": age, "class": class_name}
        )

        self.update_table()
        self.clear_form()
        QMessageBox.information(self, "Thành công", "Đã thêm học sinh mới!")

    def update_student(self):
        student_id = self.id_input.text()

        if not student_id:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn học sinh cần cập nhật!")
            return

        for student in self.students:
            if student["id"] == student_id:
                student["name"] = self.name_input.text()
                student["age"] = self.age_input.text()
                student["class"] = self.class_input.text()
                break

        self.update_table()
        self.clear_form()
        QMessageBox.information(self, "Thành công", "Đã cập nhật thông tin học sinh!")

    def delete_student(self):
        student_id = self.id_input.text()

        if not student_id:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn học sinh cần xóa!")
            return

        reply = QMessageBox.question(
            self,
            "Xác nhận",
            "Bạn có chắc chắn muốn xóa học sinh này?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.students = [s for s in self.students if s["id"] != student_id]
            self.update_table()
            self.clear_form()
            QMessageBox.information(self, "Thành công", "Đã xóa học sinh!")

    def clear_form(self):
        self.id_input.clear()
        self.name_input.clear()
        self.age_input.clear()
        self.class_input.clear()

    def load_student(self, item):
        row = item.row()
        self.id_input.setText(self.table.item(row, 0).text())
        self.name_input.setText(self.table.item(row, 1).text())
        self.age_input.setText(self.table.item(row, 2).text())
        self.class_input.setText(self.table.item(row, 3).text())

    def update_table(self):
        self.table.setRowCount(len(self.students))
        for i, student in enumerate(self.students):
            self.table.setItem(i, 0, QTableWidgetItem(student["id"]))
            self.table.setItem(i, 1, QTableWidgetItem(student["name"]))
            self.table.setItem(i, 2, QTableWidgetItem(student["age"]))
            self.table.setItem(i, 3, QTableWidgetItem(student["class"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentManagementSystem()
    window.show()
    sys.exit(app.exec())
