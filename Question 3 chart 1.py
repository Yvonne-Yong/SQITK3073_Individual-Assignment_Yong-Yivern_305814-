import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. 定義 5 隻股票的 Ticker
tickers = ['1155.KL', '1295.KL', '5347.KL', '1023.KL', '5225.KL']

print("Downloading fixed May-to-June historical data for Chart 1...")
# 鎖死時間窗口，並隱藏星號進度條
data = yf.download(tickers, start='2026-05-04', end='2026-06-05', progress=False)['Close']

# 清理空值
data = data.dropna()

# ==========================================================
# Chart 1: Closing Price Trend
# ==========================================================
plt.figure(figsize=(10, 6))

# 使用迴圈自動為每隻股票畫出一條獨立的折線
for ticker in tickers:
    plt.plot(data.index, data[ticker], marker='o', linewidth=2, label=ticker)

# 加上題目要求的核心元素
plt.title('Chart 1: 1-Month Closing Price Trend Comparison (Bursa Malaysia)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Date', fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel('Closing Price (RM)', fontsize=12, fontweight='bold', labelpad=10)

# 自動旋轉 X 軸的日期標籤，防止重疊
plt.xticks(rotation=45)

# 加上網格線和圖例
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', shadow=True)

plt.tight_layout()

print("Displaying Chart 1... Please close the window to complete the script.")
plt.show()