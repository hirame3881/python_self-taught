import csv

with open("130_st.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))

