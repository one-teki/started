import streamlit as st
import random

def get_fortune():
    fortunes = ["大吉", "中吉", "小吉", "吉", "凶", "大凶"]
    return random.choice(fortunes)

st.title('おみくじアプリ')
if st.button('おみくじを引く'):
    fortune = get_fortune()
    st.header(f"あなたの運勢は：{fortune}")
