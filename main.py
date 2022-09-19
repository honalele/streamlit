from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlitホームページ")

st.write("This is a demo of streamlit ")

df = pd.DataFrame({
    "1列目": [1, 5, 3, 2],
    "2列目": [10, 20, 30, 40],
})


"""
# Chapter 1: テキストの表示
### 1. ソースコードの表示

```python
import streamlit as st
import numpy as np
import pandas as pd

``` 
### 2. テーブルの表示
"""
st.table(df.style.highlight_min(axis=0))


"""
# Chapter 2: チャートの表示
### 1. 折れ線グラフ
"""
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['col1', 'col2', 'col3']
)
st.line_chart(df)
"""
### 2. エリア線グラフ
"""
st.area_chart(df)
"""
### 3. 棒グラフ
"""
st.bar_chart(df)

"""
### 4. 地図表示
"""
df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] +[35.05922, 136.98880],
    columns=['lat', 'lon']
)

st.map(df2)


"""
### 5. 画像表示
"""
img = Image.open("nana.png")
st.image(img, caption="漫画ナナ", use_column_width=True)