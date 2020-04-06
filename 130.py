import csv

with open("130_st.csv","w",newline="")as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])

