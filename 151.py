class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print("Created!")
#ここまでクラスの定義。オブジェクトはまだない

or1 = Orange(10,"dark orange")
#オブジェクトの追加

print(or1)
print(or1.weight)

or1.weight=100
or1.color="light orange"
#属性値の変更
print(or1.weight)
print(or1.color)

or2=Orange(8,"dark orange")
or3=Orange(14,"yellow")
