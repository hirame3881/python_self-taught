with open("126_st.txt","r") as f:
    print(f.read())

with open("126_st2.txt","r",encoding="utf-8") as g:
    print(g.read())
    print(g.read())

my_list=[]
with open("126_st.txt","r") as f:
    my_list.append(f.read())
print(my_list)
