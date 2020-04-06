x=["Do you want to join? Yes/No","Do you follow me? Yes/No"]
n=0
while True:
    a=input(x[n])
    if a=="Yes":
        print("That's nice!")
        break
    else:
        n=(n+1)%2
