'''
uv run streamlit run yhoo_finance_02.py
'''

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf
from plotly.subplots import make_subplots


def calculate_rolling_volatility(
    prices: pd.Series, period: int, trading_days: int = 252
) -> pd.Series:
    """Calculates rolling annualized volatility for a given day period."""
    daily_returns = prices.pct_change()
    rolling_std = daily_returns.rolling(window=period).std()
    return rolling_std * np.sqrt(trading_days)


@st.cache_data
def get_the_data() -> pd.DataFrame:
    """read the data and return a dataframe"""
    ftse100 = yf.Ticker("^FTSE")
    return ftse100.history(period="1y")


@st.cache_data
def load_data(source: str = "web") -> pd.DataFrame:
    if source == "csv":
        df = pd.read_csv("df.csv")
    elif source == "web":
        df = get_the_data()
    else:
        raise ValueError(
            f"Invalid source '{source}'. Expected 'csv' or 'web'."
        )

    df.columns = df.columns.str.strip()

    if df.index.name == "Date" or "Date" not in df.columns:
        df = df.reset_index()

    df["Date"] = pd.to_datetime(df["Date"])

    # Calculate rolling volatility columns
    df["Vol_20D"] = calculate_rolling_volatility(df["Close"], period=20)
    df["Vol_60D"] = calculate_rolling_volatility(df["Close"], period=60)

    return df


def display_metrics(df: pd.DataFrame) -> None:
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    latest_close = df["Close"].iloc[-1]
    prev_close = df["Close"].iloc[-2]
    change = latest_close - prev_close
    pct_change = (change / prev_close) * 100

    vol_20d = df["Vol_20D"].iloc[-1]
    vol_60d = df["Vol_60D"].iloc[-1]

    col1.metric("Latest Close", f"{latest_close:,.2f}", f"{change:+.2f} ({pct_change:+.2f}%)")
    col2.metric("High", f"{df['High'].iloc[-1]:,.2f}")
    col3.metric("Low", f"{df['Low'].iloc[-1]:,.2f}")
    col4.metric("Volume", f"{int(df['Volume'].iloc[-1]):,}")
    col5.metric("20D Volatility", f"{vol_20d:.2%}" if pd.notna(vol_20d) else "N/A")
    col6.metric("60D Volatility", f"{vol_60d:.2%}" if pd.notna(vol_60d) else "N/A")


def display_chart(df: pd.DataFrame) -> None:
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


def main() -> None:
    st.set_page_config(page_title="Financial Data Viewer", layout="wide")
    st.title("📈 Stock Price Dashboard")

    df = load_data()

    display_metrics(df)
    display_chart(df)

    with st.expander("View Raw Data"):
        st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()