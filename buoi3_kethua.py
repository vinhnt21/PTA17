# class Vehicle:
#     def __init__(self, model, color, price):
#         self.model = model
#         self.color = color
#         self.price = price

#     def change_color(self, new_color):
#         self.color = new_color


# class Car(Vehicle):
#     def __init__(self, model, color, price, capacity, energy_type):
#         super().__init__(model, color, price)
#         self.capacity = capacity
#         self.energy_type = energy_type


# class Container(Vehicle):
#     def __init__(self, model, color, price, capacity, maximum_load):
#         super().__init__(model, color, price)
#         self.capacity = capacity
#         self.maximum_load = maximum_load


# c = Car("Toyota", "Black", 100000, 5, "Gasoline")
# print(c.color)
# c.change_color("Pink")
# print(c.color)

# a = Container("Toyota", "Red", 100000, 5, 1000)
# print(a.color)
# a.change_color("Pink")
# print(a.color)


class Vehicle:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def change_color(self, new_color):
        self.color = new_color


class Car(Vehicle):
    def __init__(self, model, color, price, capacity, energy_type):
        super().__init__(model, color, price)
        self.capacity = capacity
        self.energy_type = energy_type


class Container(Vehicle):
    def __init__(self, model, color, price, capacity, maximum_load):
        super().__init__(model, color, price)
        self.capacity = capacity
        self.maximum_load = maximum_load


c = Car("Toyota", "Black", 100000, 5, "Gasoline")
print(c.color)
c.change_color("Pink")
print(c.color)
