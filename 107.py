tv=['GOT', 'Narcos', 'Vice']
for i,new in enumerate(tv):
    new=tv[i]
    new=new.upper()
    tv[i]=new
print(tv)

#何が起こっているか可視化
tv=['GOT', 'Narcos', 'Vice']
for i,new in enumerate(tv):
    print(i)
    print(new)
for i in enumerate(tv):
    print(i)
#後者のはtupleで出てくる
