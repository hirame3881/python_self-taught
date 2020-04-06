#1
guiter=["Hina","Sayo","Kaoru"]
for gt in guiter:
    print(gt)

#2
for i in range(25,51):
    print(i)

#3
guiter=["Hina","Sayo","Kaoru"]
for i,gt in enumerate(guiter):
    print(i)
    print(gt)

#4
sosuu=[2,3,5,7,11,13,17,19]
while True:
    answer=input("your answer")
    if answer=="q":
        break
    try:
        answer=int(answer)
        if answer in sosuu:
            print("right")
        else:
            print("wrong")
    except ValueError:
        print("input int or q to quit")
#int()とtryで非intを分けている

#5
list1=[8,19,148,4]
list2=[9,1,33,83]
added=[]
for i in list1:
    for j in list2:
        added.append(i*j)

print(added)

