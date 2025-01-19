# Class

## Khái niệm:

- Là bản mô tả của một đối tượng:

  - Thuộc tính (Được liệt kê ở hàm `__init__`)
  - Hành vi

- Ví dụ:

  ```python
  class Student:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def do_homework(self):
          print(self.name + " is doing homework")
  ```

## Kế thừa

- Class cha có gì thì class con có cái đó

- Ví dụ:

  ```python
  class Vehicle:
      def __init__(self, name, color):
          self.name = name
          self.color = color

      def drive(self):
          print(self.name + " is driving")


  class Bus(Vehicle):
      def __init__(self, name, color, price):
          super().__init__(name, color)
          self.price = price

      def drive(self):
          print(self.name + " is driving slowly")

  ```

---

# PyQT6

- PyQT6 là một thư viện Python dùng để tạo giao diện đồ họa

## QT Designer

## Prompt template tạo style sheet

```plaintext
Tôi muốn tạo một style sheet cho một ui tạo bởi QT Designer

Nhiệm vụ: Cung cấp style sheet code để tạo giao diện theo yêu cầu dưới, chỉ trả về code style sheet

Giao diện gồm:
{Liệt kê các thành phần}

Yêu cầu:
{Liệt kê yêu cầu}
```

## Ví dụ

```plaintext
Tôi muốn tạo một style sheet cho một ui tạo bởi QT Designer

Nhiệm vụ: Cung cấp style sheet code để tạo giao diện theo yêu cầu dưới, chỉ trả về code style sheet

Giao diện gồm:
- Button
- Label
- Line Edit

Yêu cầu:
- Button: Màu nền gradient từ màu xanh đến màu đỏ, chữ màu trắng viền màu đen nổi bật
- Label: Nền màu đỏ, chữ màu trắng
- Line Edit: Nền màu xanh, chữ màu trắng
```

