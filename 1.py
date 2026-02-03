import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["font.sans-serif"] = [
    "PingFang TC",
    "Heiti TC",
    "Noto Sans CJK TC",
    "Arial Unicode MS"
]
plt.rcParams["axes.unicode_minus"] = False


pe_values = [
    67.68,73.08,66.11,45.78,30.38,38.77,43.46,34.50,46.08,52.40,58.93,50.95,
    48.28,55.62,50.06,44.73,42.05,35.87,29.50,33.38,40.12,32.25,35.46,36.38,
    36.45,40.40,43.98,49.47,52.51,63.69,73.78,68.06,80.77,84.57,83.76,91.35,
    99.88,110.80,81.21,67.58,55.92,53.93,53.50,40.12,38.06,31.87,31.86,40.96,
    42.10,47.70,36.00,27.66,31.99,33.97,43.11,49.74,47.29,41.20,45.77,44.24
]

dates = pd.date_range("2021-01-01", periods=len(pe_values), freq="MS")
pe = pd.Series(pe_values, index=dates)

# -------------------------------
# 統計計算
# -------------------------------
pe_mean = pe.mean()
pe_std = pe.std()

# -------------------------------
# 畫圖
# -------------------------------
plt.figure(figsize=(14, 8))

# ±2σ（最外層）
plt.fill_between(
    pe.index,
    pe_mean - 2 * pe_std,
    pe_mean + 2 * pe_std,
    color="#b3cde3",
    alpha=0.45,
    label="±2 標準差"
)

# ±1σ（內層）
plt.fill_between(
    pe.index,
    pe_mean - pe_std,
    pe_mean + pe_std,
    color="#6497b1",
    alpha=0.55,
    label="±1 標準差"
)

# 平均本益比
plt.plot(
    pe.index,
    [pe_mean] * len(pe),
    color="#03396c",
    linestyle="--",
    linewidth=2.5,
    label=f"平均本益比：{pe_mean:.2f}"
)

# 每月本益比線
plt.plot(
    pe.index,
    pe,
    color="#ff6f00",
    linewidth=2.8,
    label="每月本益比"
)

# -------------------------------
# 圖表設定
# -------------------------------
plt.title("世芯-KY（3661）本益比標準差分析（2021–2025）", fontsize=16)
plt.ylabel("本益比")
plt.xlim(pe.index.min(), pe.index.max())
plt.grid(alpha=0.3)
plt.legend(frameon=False)
plt.margins(x=0)
plt.tight_layout()
plt.show()
