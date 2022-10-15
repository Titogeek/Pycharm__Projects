# Defining Classes in Python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def jump(self):
        print("jump")


point2 = Point(10,20)
print(point2.x)


# Exersice- Just For Laughs
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"My name is {self.name}")


Annabelle = Person("Shiko Murigi")
Annabelle.talk()




