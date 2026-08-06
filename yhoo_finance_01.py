'''
uv run streamlit run yhoo_finance_01.py
'''


import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf
from plotly.subplots import make_subplots

st.set_page_config(page_title="Financial Data Viewer", layout="wide")

st.title("📈 Stock Price Dashboard")

def get_the_data():
    ftse100 = yf.Ticker("^FTSE")
    df = ftse100.history(period="1y")
    return df
    
# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("df.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# Summary Metrics
col1, col2, col3, col4 = st.columns(4)
latest_close = df["Close"].iloc[-1]
prev_close = df["Close"].iloc[-2]
change = latest_close - prev_close
pct_change = (change / prev_close) * 100

col1.metric("Latest Close", f"{latest_close:,.2f}", f"{change:+.2f} ({pct_change:+.2f}%)")
col2.metric("High", f"{df['High'].iloc[-1]:,.2f}")
col3.metric("Low", f"{df['Low'].iloc[-1]:,.2f}")
col4.metric("Volume", f"{int(df['Volume'].iloc[-1]):,}")

# Interactive Plotly Figure
fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    row_heights=[0.7, 0.3],
)

# Candlestick chart
fig.add_trace(
    go.Candlestick(
        x=df["Date"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="OHLC",
    ),
    row=1,
    col=1,
)

# Volume bar chart
fig.add_trace(
    go.Bar(
        x=df["Date"],
        y=df["Volume"],
        name="Volume",
        marker_color="rgba(100, 150, 250, 0.5)",
    ),
    row=2,
    col=1,
)

fig.update_layout(
    xaxis_rangeslider_visible=False,
    template="plotly_white",
    height=600,
    margin={"l": 20, "r": 20, "t": 20, "b": 20},
)

st.plotly_chart(fig, use_container_width=True)

# Data Table Display
with st.expander("View Raw Data"):
    st.dataframe(df, use_container_width=True)