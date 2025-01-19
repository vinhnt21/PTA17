class Singer:
    def __init__(self, name, age, height, weight, gender):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender


jack = Singer("Tuan Trinh Tran Phong", 27, 170, 60, "Male")
thang = Singer("Vu Dinh Trong Kien", 18, 190, 80, "Male")


print(jack.name)
print(thang.name)


