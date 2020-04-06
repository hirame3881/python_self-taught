trans={"Apple":"りんご",
       "Grape":"ぶどう",

"Orange":"オレンジ"
       }
#こんなにガタガタでもなんとかなるのか...
inp=input("英語を入力")

if inp in trans:
    print(trans[inp])
else:
    print("データ無し")
