# # 1
# # Я сравнивал классы по их оперативной памяти
#
# class Computer:
#     def __init__(self, owner: str, op_memory):
#         self.owner = owner
#         self.op_memory = op_memory
#     def __str__(self):
#         return f"Владельцем компьютера является {self.owner}"
#
#     def __repr__(self):
#         return f"Владельцем компьютера является {self.owner}"
#
# class Computer2:
#     def __init__(self, name: str, op_memory):
#         self.op_memory = op_memory
#         self.name = name
#     def __str__(self):
#         return f"Владельцем другого компьютера является {self.name}"
#
#     def __repr__(self):
#         return f"Владельцем другого компьютера является {self.name}"
#
# comp = Computer("Мухаммадсодик", 32)
# comp2 = Computer2("Озод", 32)
# print(comp)
# print(comp2)
#
# if (comp.op_memory == comp2.op_memory) == True:
#     print(f"Операционная памяти этих компьютеров равны, т.к {comp.op_memory} gb = {comp2.op_memory} gb")
# elif (comp.op_memory > comp2.op_memory) == True:
#     print(f"Операционная память {comp.owner} лучше, т.к {comp.op_memory} gb > {comp2.op_memory} gb")
# elif (comp.op_memory < comp2.op_memory) == True:
#     print(f"Операционная память {comp2.name} лучше, т.к {comp2.op_memory} gb > {comp.op_memory} gb")

# 2
# class Animals:
#     def __init__(self, birds, mammals, reptiles, fish):
#         self.birds = birds
#         self.mammals = mammals
#         self.reptiles = reptiles
#         self.fish = fish
# class Birds(Animals):
#     def __init__(self, color, residence, wingspan, eat):
#         super().__init__(color, residence, wingspan, eat)
#         self.color = color
#         self.residence = residence
#         self.wingspan = wingspan
#         self.eat = eat
# eagle = Birds("Темно-коричневый", "В степях и полупустынях", "1.8-2.3 m", "Иногда питается молодыми сурками, зайцами и любыми курообразными")
# chicken = Birds("Белые", "В фермах", "1 m", "Семенами и травой")
#
# class Mammals(Animals):
#     def __init__(self, color, residence, size, eat):
#         super().__init__(color, residence, size, eat)
#         self.color = color
#         self.residence = residence
#         self.size = size
#         self.eat = eat
# rat = Birds("Серые", "Пастбищах", "8 - 30 cm", "Животный белок")
# monkey = Birds("Коричневые", "В тропических лесах", "55 - 65 cm", "Почти все что мы едим")
#
# class Reptiles(Animals):
#     def __init__(self, residence, scale_size, size, eat):
#         super().__init__(residence, scale_size, size, eat)
#         self.residence = residence
#         self.scale_size = scale_size
#         self.size = size
#         self.eat = eat
# snake = Birds("В лесах и в местах где много травы", "2 - 3 m", "2 - 3 m", "Мясо")
# chameleon = Birds("Во всех видах тропических лесов", "20 cm", "20 cm", "Насекомые")
#
# class Fish(Animals):
#     def __init__(self, residence, color, eat):
#         super().__init__(residence, color, eat) # Parameter 'fish' unfilled
#         self.residence = residence
#         self.color = color
#         self.eat = eat
# clownfish = Birds("Вода", "Любого цвета", "Сухой мотыль") # Parameter 'eat' unfilled
# white_shark = Birds("Вода", "Белые", "Мясо") # Parameter 'eat' unfilled
# # Не могу исправить эти проблемы, вроде все правильно же

# 3
class Figures:
    def __init__(self, triangle, square, circle):
        self.triangle = triangle
        self.square = square
        self.circle = circle

class Triangle(Figures):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c

class Square(Figures):
    def __init__(self, a, b):
        super().__init__(a, b)


perimeter = Triangle(1, 2, 3)
print(f"{perimeter.perimeter()} - периметер треугольника")



