#1
with open("126_st2.txt","r",encoding="utf-8")as f:
    print(f.read())
#2
x=input("What is your name?")
with open("132_name.txt","w",encoding="utf-8") as g:
    g.write(x)

#3
import csv
list1=[["Yukina","Sayo","Risa"],
       ["Chisato","Hina","Eve"],
       ["Kokoro","Kanon","Kaoru"]]

with open("132_members.csv","w",newline="") as h:
    w=csv.writer(h,delimiter=",")
    for li in list1:
        w.writerow(li)
#newlineを入れてやらないとなんか１行ずつ空く

#4
import csv
list1=[["友希那","紗夜","リサ"],
       ["千聖","日菜","イヴ"],
       ["こころ","花音","薫"]]

with open("132_membersJP.csv","w",encoding="Shift_JIS",newline="") as h:
    w=csv.writer(h,delimiter=",")
    for li in list1:
        w.writerow(li)
#newlineを入れてやらないとなんか１行ずつ空く
#encodingなしでいける。utf-8入れると逆に文字化けする。shift_jisだと正常　なにこれ？
