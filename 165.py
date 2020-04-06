class Shape:
    def __init__(self,w,l):
        self.width =w
        self.len =l
    def print_size(self):
        print("{} by {}".format(self.width,self.len))
              
class Square(Shape):
    pass

a_square = Square(20,30) #Squareに引数２つで定義してよい
a_square.print_size()#printで囲わなくてよい
              
class Square2(Shape):
    def area(self):
        return self.width * self.len

a_square2 = Square2(10,6)
print(a_square2.area())


class Square3(Shape):
    def print_size(self):
        print("I am {} by {}".format(self.width,self.len))

a_square3 = Square3(2,7)
a_square3.print_size()
#親はそのまま↓
a_square1 = Square(3,5)
a_square1.print_size()

