import yfinance as yf
import pandas as pd

# 1. 核心資產配置與鎖定時間邊界
tickers = ['1155.KL', '1295.KL', '5347.KL', '1023.KL', '5225.KL']
investment_capital = 1000.00

# 鎖死與第一題完全一致的 5 月份歷史數據區間，並關閉進度條
historical_data = yf.download(tickers, start='2026-05-04', end='2026-06-05', progress=False)['Close']
historical_data = historical_data.dropna()

yesterday_prices = historical_data.iloc[-2]
today_prices = historical_data.iloc[-1]

# 2. 生成主數據矩陣
portfolio_records = []
for ticker in tickers:
    yest_p = round(float(yesterday_prices[ticker]), 2)
    today_p = round(float(today_prices[ticker]), 2)
    daily_return = round(today_p - yest_p, 2)
    shares_purchased = round(investment_capital / yest_p, 2)
    estimated_return = round(shares_purchased * daily_return, 2)
    return_percentage = round((daily_return / yest_p) * 100, 2)
    
    portfolio_records.append({
        'Ticker': ticker,
        'Yesterday Closing Price': yest_p,
        'Today Closing Price': today_p,
        'Estimated Total Return': estimated_return,
        'Return Percentage': return_percentage
    })

df_main = pd.DataFrame(portfolio_records)

# ==========================================================
# Question 2(a): Data Filtering Using pandas Slicing
# ==========================================================
# 嚴格執行題目要求，只保留 5 個核心欄位並重新命名
columns_to_keep = ['Ticker', 'Yesterday Closing Price', 'Today Closing Price', 'Estimated Total Return', 'Return Percentage']
df_summary = df_main[columns_to_keep].rename(columns={
    'Yesterday Closing Price': 'Previous Closing Price',
    'Today Closing Price': 'Latest Closing Price'
})

print("### Question 2(a): Portfolio Summary Table ###")
print(df_summary.to_string(index=False))
print("==========================================================\n")