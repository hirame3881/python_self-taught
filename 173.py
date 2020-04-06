class Lion:
    def __init__(self,name):
        self.name =name

lion =Lion("Dilbert")
print(lion)

class Pig:
    def __init__(self,name):
        self.name =name
    def __repr__(self):
        return self.name 
pig =Pig("Alpha")
print(pig)
