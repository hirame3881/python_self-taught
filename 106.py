tv=["GOT","Narcos","Vice"]
i=0
for show in tv:
    new=tv[i]
    new=new.upper()
    tv[i]=new
    i+=1
print(tv)
#これだとiは１ループ中ずっと変わらないという利点がある


#↓だとリストを変更できない
tv=["GOT","Narcos","Vice"]
i=0
for show in tv:
    show=show.upper()
print(tv)


#↓なら大丈夫。showをupperする前にindに入れること
tv=["GOT","Narcos","Vice"]
i=0
for show in tv:
    ind=tv.index(show)
    tv[ind]=show.upper()
print(tv)
