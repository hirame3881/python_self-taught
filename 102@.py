#1
print("カミュ"[0])
print("カミュ"[1])
print("カミュ"[2])

#2
x=input("write")
y=input("person")
print("私は昨日{}を書いて{}に送った".format(x,y))

#3
print("aldous Huxley was born in 1894".capitalize())
#title()で単語頭

#4
print("どこで? だれが? いつ?".split( ))

#5
x=["The","fox","jumped","over","."]
y=" ".join(x)
print(y)
#解答はこれに加えて
y=y[0: -2] + "."
print(y)

#6
print("A screaming comes across the sky".replace("s","$"))

#7
print("Hemingway".index("m"))

#8
print('こいつには、やると言ったらやる………\'スゴ味\'があるッ！')

#9
x="three "
print(x+x+x.strip())
print(x*3.strip())
#一回x*3を変数に入れるだけ
y=x*3
print(y.strip())

#10
print("四月の晴れた寒い日で、時計"[:10])

