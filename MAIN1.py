import streamlit as st

st.title("Welcome to my hard earned website")
st.header("Python")
st.subheader("Java")
st.markdown("I love python")
st.code("""for i in range(1,5,1):
                print("Hello")
        """)
import pandas as pd

dataset1 = pd.read_csv("EXCEL_PRACTICE_20_MARCH_2025.csv")

st.dataframe(dataset1)

name = st.text_input("Enter your name")
fname = st.text_input("Enter your Father's name")
adr = st.text_input("Enter your Text: ")
classdata = st.selectbox("Enter your Class :",(1,2,3,4,5,6))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name: {name}
    Father Name : {fname}
    address : {adr}
    class : {classdata}
""")
