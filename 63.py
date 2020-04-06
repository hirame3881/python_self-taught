x=100

def f():
    global x
    x+=1
    print(x)


f()
f()
f()
print(x)

#書き込みは関数内だけで留まるものではない
