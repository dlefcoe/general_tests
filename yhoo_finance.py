# %%
import yfinance as yf

# FTSE 100 symbol: ^FTSE | FTSE 250 symbol: ^FTMC
ftse100 = yf.Ticker("^FTSE")
df = ftse100.history(period="1y")


# %%
print(df.tail())


