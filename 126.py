st=open("126_st.txt","w")
st.write("Hi from Python!")
st.close()
#何回やっても上書きはしないっぽい

with open("126_st.txt","w") as st:
    st.write("Hi from Python")

st2=open("126_st2.txt","w",encoding="utf-8")
st2.write("Pythonからこんにちは")
st2.close()
