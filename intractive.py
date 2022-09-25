from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit インタラクティブ超入門')

st.write('Display Image')


"""
# Chapter 3: Intractive
### 1. チェックボックス
"""
if st.checkbox("Show Image"):
    img = Image.open("nana.png")
    st.image(img, caption="漫画ナナ", use_column_width=True)
    

"""
### 2. セレクトボックス
"""
option =  st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は：　', option, 'です。'