import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['1155.KL', '1295.KL', '5347.KL', '1023.KL', '5225.KL']

print("Downloading fixed May-to-June historical data for Chart 1...")

data = yf.download(tickers, start='2026-05-04', end='2026-06-05', progress=False)['Close']

data = data.dropna()

plt.figure(figsize=(10, 6))

for ticker in tickers:
    plt.plot(data.index, data[ticker], marker='o', linewidth=2, label=ticker)

plt.title('Chart 1: 1-Month Closing Price Trend Comparison (Bursa Malaysia)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Date', fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel('Closing Price (RM)', fontsize=12, fontweight='bold', labelpad=10)

plt.xticks(rotation=45)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', shadow=True)

plt.tight_layout()

print("Displaying Chart 1... Please close the window to complete the script.")
plt.show()