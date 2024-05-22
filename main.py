import streamlit as st 

st.text("hello world")

number = st.number_input("이름을 입력하세요!")
st.write(f'현재 숫자는 {number}입니다.')
