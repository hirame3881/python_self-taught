#1
class Apple:
    def __init__(self,x,y,z,a):
        self.weight = x
        self.color = y
        self.kind =z
        self.country =a

apple1 = Apple(240,"blue","Fuji","Japan")

print(apple1.kind)

#2
import math
class Circle:
    def __init__(self,r):
        self.radius =r
    def area(self):
        #クラス内メソッドには引数selfが必要
        return math.pi * (self.radius) **2

circle1 = Circle(3)
print(circle1.area())

#3
class Triangle:
    def __init__(self,b,h):
        self.bottom =b
        self.height =h
    def area(self):
        return 1/2 * self.bottom * self.height

triangle1 =Triangle(10,4)
print(triangle1.area())

#4
class Hexagon:
    def __init__(self,l):
        self.length =l
    def calculate_perimeter(self):
        return 6*self.length

hexagon1 =Hexagon(7)
print(hexagon1.calculate_perimeter())
