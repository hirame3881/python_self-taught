class Person:
    def __init__(self):
        self.name ="Bob"

bob = Person()
same_bob = bob
print(same_bob is bob)

another_bob = Person()
print(another_bob is bob)



x =10
if x is None:
    print("x is None")
else:
    print("x isn't None")

x=None
if x is None:
    print("x is None")
else:
    print("x isn't None")
