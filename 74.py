colors=["blue","green","yellow"]
item=colors.pop()
#colorsに.popでメソッド。()に入れ込む。それの変数がitem
print(item)
print(colors)
item_container=[colors.pop()]
print(item_container)
colors.pop()
#変数置かなくてもpopだけで切り取れる
print(colors)

fruit1=("Banana","Apple")
fruit2=(100,True)
print(fruit1+fruit2)
fruit3=fruit1+fruit2
print(fruit3)
fruit4=("Banana")
print(fruit4)
