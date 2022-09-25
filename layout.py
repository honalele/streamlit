from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit レイアウト入門')

"""Progress Bar 
    """
"ゲームスタート!"
latest_iteration = st. empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    time.sleep(0.01)
    bar.progress(i+1)
"ロード完了!"

"""カラム
    """    
left_column,right_column = st.columns(2)
left_button = left_column.button("右カラムに文字を表示")
if left_button:
    right_column.write("ここは右カラム")
    
"""expander
    """
expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ内容を書く")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ内容を書く")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ内容を書く")

