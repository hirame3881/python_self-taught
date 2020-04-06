class Card:
    suits =["speads","hearts","diamonds","clubs"]
    values =[None,None,"2","3","4","5","6","7","8","9",
             "10","Jack","Queen","King","Ace"]
    def __init__(self,v,s):
        """suit,value共に整数値"""
        self.value =v
        self.suit =s
    def __lt__(self,c2):
        """self < other と比較演算子が与えられた時のための特殊メソッド"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
            #この場合、何かのミスで同じカードを＜で比較するとFalseが返ってくる
        return False
        #ここのelseは省略（？）。多分if内にreturnがあるから出来る
    
    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit>self.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v

def test_card():
    """Cardクラスのテスト用"""
    card1 = Card(10,2)
    card2 = Card(11,3)
    print(card1 < card2)
    print(card1 > card2)
    print(card1)



from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def rm_card(self):
        """suffleした山札を１つずつ消しながら返す"""
        if len(self.cards) ==0:
            return
            #これでNoneが返る
        return self.cards.pop()

def test_deck():
    deck = Deck()
    for card in deck.cards: #cardsは５２枚のリスト
        print(card)



class Player:
    def __init__(self,name):
        self.wins =0
        self.card =None
        self.name =name



class Game:
    def __init__(self):
        name1 =input("プレーヤー１の名前 ")
        name2 =input("プレーヤー２の名前 ")
        self.deck =Deck()
        self.p1 =Player(name1)#イン変数nameにname1を持つPlayerクラスのobject
        self.p2 =Player(name2)
    def wins(self,winner):
        w ="このラウンドは{}が勝ちました"
        w =w.format(winner)
        print(w)
    def draw(self,p1n,p1c,p2n,p2c):
        d ="{}は{}、{}は{}を引きました"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)
    def play_game(self):
        cards =self.deck.cards #deckはDeckの唯一のオブジェクト。.cardsで中身のカードリスト
        print("戦争を始めます")
        while len(cards) >= 2:
            m ="qで終了、それ以外のキーでPlay"
            response =input(m)
            if response =="q":
                break
            p1c =self.deck.rm_card()
            p2c =self.deck.rm_card()
            p1n =self.p1.name
            p2n =self.p2.name
            self.draw(p1n,p1c,p2n,p2c) #draw関数は通知だけ
            if p1c>p2c: #Cardクラスなので比較できる
                self.p1.wins +=1
                self.wins(self.p1.name) #通知
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)
        #感覚的にはここにwinner関数処理が入る
        winpl = self.winner(self.p1,self.p2)
        print("ゲーム終了、{}の勝利です".format(winpl))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins > p2.wins:
            return p2.name
        return "引き分け"



game =Game()
game.play_game()
