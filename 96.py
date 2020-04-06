equ="All animals are"
equ2=equ.replace("a","@")
print(equ2)


number="animals".index("m")
print(number)

try:
    "animals".index("z")
except:
    print("not found")
#exceptこれで拾えるのか
