import streamlit as st 

st.text("hello world")

text = st.text_input("이름을 입력하세요!")
st.write("반갑습니다! " + text + "님!")
