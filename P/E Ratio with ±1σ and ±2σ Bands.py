import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 從財報狗抓 2021-2025 逐月本益比
PE_Ratio = [
    67.68,73.08,66.11,45.78,30.38,38.77,43.46,34.50,46.08,52.40,58.93,50.95,
    48.28,55.62,50.06,44.73,42.05,35.87,29.50,33.38,40.12,32.25,35.46,36.38,
    36.45,40.40,43.98,49.47,52.51,63.69,73.78,68.06,80.77,84.57,83.76,91.35,
    99.88,110.80,81.21,67.58,55.92,53.93,53.50,40.12,38.06,31.87,31.86,40.96,
    42.10,47.70,36.00,27.66,31.99,33.97,43.11,49.74,47.29,41.20,45.77,44.24
]

dates = pd.date_range("2021-01-01", periods=len(PE_Ratio), freq="MS")
PE = pd.Series(PE_Ratio, index=dates)


# 本益比平均值、標準差
PE_mean = PE.mean()
PE_std = PE.std()


plt.figure(figsize=(14, 8))

# ±2σ
plt.fill_between(
    PE.index,
    PE_mean - 2 * PE_std,
    PE_mean + 2 * PE_std,
    color="#96c2e6",
    alpha=0.55,
    label="±2σ"
)

# ±1σ
plt.fill_between(
    PE.index,
    PE_mean - PE_std,
    PE_mean + PE_std,
    color="#87d7ff",
    alpha=0.45,
    label="±1σ"
)

# 平均本益比
plt.plot(
    PE.index,
    [PE_mean] * len(PE),
    color="#03396c",
    linestyle="--",
    linewidth=2.5,
    label=f"Average P/E Ratio: {PE_mean:.2f}")


# 逐月本益比線
plt.plot(
    PE.index,
    PE,
    color="#ff6f00",
    linewidth=2.8,
    label="Monthly P/E Ratio"
)

# 圖表設定
plt.title("Alchip P/E Ratio with ±1σ and ±2σ Bands", fontsize=16)
plt.ylabel("P/E Ratio")
plt.xlim(PE.index.min(), PE.index.max())
plt.grid(alpha=0.3)
plt.legend(frameon=False)
plt.margins(x=0)
plt.tight_layout()
plt.show()
