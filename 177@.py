#1
class Square:
    square_list =[]
    def __init__(self,l):
        self.len =l
        self.square_list.append(self)

square1 =Square(4)
square2 =Square(8)
square3 =Square(12)
print(Square.square_list)

#2
class Square:
    def __init__(self,l):
        self.len =l
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len,self.len,self.len,self.len)

square11 =Square(10)
print(square11)


#3
def diff(x,y):
    return x is y
    
