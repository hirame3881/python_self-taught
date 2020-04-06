class APositive:
    def __init__(self,number):
        self.n =number
    def __add__(self,other):
        return abs(self.n + other.n)

x =APositive(-20)
y =APositive(10)
print(x+y)
