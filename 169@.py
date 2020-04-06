#1
class Shape:
    def __init__(self,w,l):
        self.width =w
        self.length =l
    def calculate_perimeter(self):
        return self.width*2 + self.length*2

class Rectangle(Shape):
    pass
    
class Square(Shape):
    pass

a_rectangle=Rectangle(20,3)
print(a_rectangle.calculate_perimeter())
a_square=Square(10,4)
print(a_square.calculate_perimeter())

#2
class Square:
    def __init__(self,w,l):
        self.width =w
        self.length =l
    def change_size(self,x,y):
        self.width+=x
        self.length+=y

a_square =Square(10,20)
a_square.change_size(2,-4)
print(a_square.width)
print(a_square.length)

#3
class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    #誤答：pass
    def __init__(self,width,length):
        self.width =width
        self.length =length
    def cal_per(self):
        return self.width*2 + self.length*2
        
    
class Square(Shape):
    pass

a_rectangle =Rectangle(20,50) #もちろん引数要る
a_square =Square()
a_rectangle.what_am_i()
a_square.what_am_i()


#4
class Rider:
    def __init__(self,name):
        self.name =name
class Horse:
    def __init__(self,name,the_rider):
        self.name=name
        self.rider =the_rider.name

a_rider =Rider("Tanaka")
a_horse =Horse("uma",a_rider)
print(a_horse.rider)
