
import re
text ="""キリンは昔から__複数名詞__の興味の対象でした。
そのような長い__体の一部__を獲得したのか説明できません。
キリンの身長は__数値__ __単位__近くあり、
その高さのほとんどは脚と__体の一部__によるものです。"""

def mad_libs(mls):
    """
    :palam mls:ヒントは２つのアンダースコアで挟んでください。
    ヒントの単語にはアンダースコアを含まないでください。
    """
    hints =re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q ="{}を入力".format(word)
            new =input(q)
            mls =mls.replace(word,new,1)
        print('\n')
        mls =mls.replace("\n","")
        print(mls)
    else:
        print("引数mlsが無効です")
mad_libs(text)
