#1
musician=["Aya","Yukina","Kokoro"]
#2
sydney_AL=("南緯33度52分06秒","東経151度12分31秒")
Tokyo_AL=("北緯36度","東経140度")
#解答：[(40.7128, 74.0059), (31.0461, 34.8516), (8.3405, 115.0920)]。「タプルのリスト」を作ろう

#3
Me={"height":178,"color":"orange","food":"natto"}
#4
#キーが入ってなかった時を分けて
K=input("chara")
if K in Me:
    print(Me[K])
else:
    print("no data")
#5
music={"aya":"luminas","yukina":"Louder"}
