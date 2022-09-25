from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit レイアウト入門')

left_column,right_column = st.columns(2)
left_button = left_column.button("右カラムに文字を表示")
if left_button:
    right_column.write("ここは右カラム")