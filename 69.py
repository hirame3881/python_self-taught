#1

def f1(x):
    """
    kore nanikaitemo iino?
    returns x^2
    :param x:int
    return:int x^2
    """
    return x**2
a= input("number 1")
print(f1(float(a)))
#ここはintでなくfloatを使おう


#2

def f2(x):
    print(x)

b= input("number2")
f2(b)
#f2をprintしなくても置くだけで起動できる。

    
#3
def f3(k,l,m,n=15,o=18):
    return k+l+m+n+o

print(f3(1,1,1))


#4

def f4(x):
    return int(int(x)/2)
def g5(y):
    return 4*int(y)

x=f4(int(input("number4")))
print(g5(x))


#5


def f5(x):
    return float(x)
c= input("number5:")
try:
    print(f5(c))
except ValueError:
    print("Invalid input")
#floatに文字列を与えているのはtry内で行われているので、この書き方でもexceptは拾える


