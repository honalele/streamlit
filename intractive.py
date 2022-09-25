from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit インタラクティブ　超入門')

st.write('Display Image')

if st.checkbox("Show Image"):
    img = Image.open("nana.png")
    st.image(img, caption="漫画ナナ", use_column_width=True)