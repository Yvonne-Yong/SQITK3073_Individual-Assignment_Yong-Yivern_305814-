import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['1155.KL', '1295.KL', '5347.KL', '1023.KL', '5225.KL']
investment_capital = 1000.00

historical_data = yf.download(tickers, start='2026-05-04', end='2026-06-05', progress=False)['Close']
historical_data = historical_data.dropna()

yesterday_prices = historical_data.iloc[-2]
today_prices = historical_data.iloc[-1]

portfolio_records = []
stock_names = {
    '1155.KL': 'Maybank',
    '1295.KL': 'Public Bank',
    '5347.KL': 'Tenaga Nasional',
    '1023.KL': 'CIMB Group',
    '5225.KL': 'IHH Healthcare'
}

for ticker in tickers:
    yest_p = round(float(yesterday_prices[ticker]), 2)
    today_p = round(float(today_prices[ticker]), 2)
    daily_return = round(today_p - yest_p, 2)
    shares_purchased = round(investment_capital / yest_p, 2)
    estimated_return = round(shares_purchased * daily_return, 2)
    
    portfolio_records.append({
        'Stock Name': stock_names[ticker],
        'Estimated Total Return': estimated_return
    })

df = pd.DataFrame(portfolio_records)

plt.figure(figsize=(9, 6))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
bars = plt.bar(df['Stock Name'], df['Estimated Total Return'], color=colors, edgecolor='black', width=0.6)

plt.title('Chart 2: Estimated Total Return Comparison per RM1,000 Investment', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Stock Name', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Estimated Total Return (RM)', fontsize=11, fontweight='bold', labelpad=10)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.4, f'RM {yval:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.ylim(0, max(df['Estimated Total Return']) + 3)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

print("Displaying Chart 2... Please close the window to complete the script.")
plt.show()