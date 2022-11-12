import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st



st.title('米国株価可視化アプリ')
st.sidebar.write("""
                 # 米国GIANTテック企業株価
                 こちらは株価可視化ウェブアプリです。以下のオプションから表示日数を指定し、確認したい会社名をお選びください。　
                 """)
st.sidebar.write("""
                 ## 表示日数選択 
                 """)
n_days = st.sidebar.slider('日数', 1, 50, 20)

st.write(f"""
         ### 過去 **{n_days}日間**の米国GIANTテック企業株価
         """)


tickers = {"apple": 'AAPL', 
           "microsoft": 'MSFT',
           "meta": 'META',
           "amazon": 'AMZN',
           "twitter": 'TWTR',
           "netflix": 'NFLX',
           "tesla": 'TSLA',
           "google": 'GOOG',
           "twillo": 'TWLO',
           "snap": 'SNAP',
           }

@st.cache
def get_data(n_days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f"{n_days}d")
        hist.index = hist.index.strftime('%d %B %Y')
        hist_close = hist[['Close']]
        hist_close.columns = [company]
        hist_close = hist_close.T
        hist_close.index.name = 'Name'
        df = pd.concat([df, hist_close])
    return df


st.sidebar.write("""
                 ## 株価の範囲指定 (USD)
                 """)
ymin, ymax = st.sidebar.slider('範囲を設定してください', 0.0, 1000.0, (0.0, 1000.0))

df = get_data(n_days,tickers)

companies = st.multiselect("株価の会社を選んでください。",
               list(df.index),
               ['google', 'amazon', 'netflix', 'meta'])

if not companies:
    st.error('少なくとも一社は選んでください。')
else:
    data = df.loc[companies]
    st.write("""### 株価 (USD)""", data.sort_index())
    data = data.T.reset_index()
    data = pd.melt(data, id_vars=['Date']).rename(columns={'value': "Stock Prices(USD)"})
    chart = (
        alt.Chart(data)
        .mark_line(opacity=0.8, clip=True)
        .encode(
            x="Date:T",
            y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
            color = 'Name:N'
        )
    )
    st.altair_chart(chart, use_container_width=True)