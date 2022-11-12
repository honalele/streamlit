import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st



st.title('米国株価可視化アプリ')
st.sidebar.write("""
                 # 米国Giantテック企業株価
                 こちらは株価可視化ウェブアプリです。以下のオプションから表示日数を指定し、確認したい会社名をお選びくダサい。　
                 # """)

# Parameter setting
n_days = 20
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
