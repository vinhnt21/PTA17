"""
Vehicle:
    - model
    - color
    - price
Car:
    - model
    - color
    - price
    - capacity
    - energy_type
Container:
    - model
    - color
    - price
    - capacity
    - maximum_load
"""


class Vehicle:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def change_color(self, new_color):
        self.color = new_color


class Car:
    def __init__(self, model, color, price, capacity, energy_type):
        self.model = model
        self.color = color
        self.price = price
        self.capacity = capacity
        self.energy_type = energy_type

    def change_color(self, new_color):
        self.color = new_color


class Container:
    def __init__(self, model, color, price, capacity, maximum_load):
        self.model = model
        self.color = color
        self.price = price
        self.capacity = capacity
        self.maximum_load = maximum_load

    def change_color(self, new_color):
        self.color = new_color


# v = Vehicle("Toyota", "Black", 100000)
# print(v.color)
# v.change_color("Pink")
# print(v.color)

c = Car("Toyota", "Black", 100000, 5, "Gasoline")
print(c.color)
c.change_color("Pink")
print(c.color)
