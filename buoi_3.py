"""
User:
- username
- password
- full_name
"""


class User:
    def __init__(self, username, password, full_name, balance):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.balance = balance

    def charge(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


duong = User("duongdz", "phong_phuong_tuan", "Nguyễn Thế Dương", 999)
print(duong.balance)
duong.charge(100)
print(duong.balance)
duong.withdraw(500)
print(duong.balance)
