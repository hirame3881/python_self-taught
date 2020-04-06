pop=[]
jpop=[]



def record():
    
    while True:
        inp=input("曲名を入力")
        state=input("input p or q. q to quit")

        if state == "p":
            pop.append(inp)
        elif state=="j":
            jpop.append(inp)
        elif state=="q":
            break
        else:
            print("input p or j or q")

    print(pop)
    print(jpop)
    print("pop songs:",pop)

record()
print(pop)


#模範145
#stateの判定（break判定)をinpより前にする
#3つめのprintでやるとスマート
