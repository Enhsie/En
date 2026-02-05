import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 下載世芯-KY 跟台灣加權指數股價
start_date = "2021-01-01"

stock = yf.download("3661.TW", start=start_date, auto_adjust=True)
index = yf.download("^TWII", start=start_date, auto_adjust=True)

if stock.empty or index.empty:
    raise ValueError("Data download failed")

data = pd.concat(
    [stock["Close"], index["Close"]],
    axis=1,
    keys=["AIChip", "Taiwan Weighted Index"]
).dropna()

#計算成長率，以 2021/01/01 為基準 100
growth = data / data.iloc[0] * 100


plt.figure(figsize=(10, 6))
plt.plot(growth.index, growth["AIChip"], label="AIChip (3661.TW)")
plt.plot(growth.index, growth["Taiwan Weighted Index"], label="Taiwan Weighted Index")

plt.xlabel("Date")
plt.ylabel("Growth Index")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
