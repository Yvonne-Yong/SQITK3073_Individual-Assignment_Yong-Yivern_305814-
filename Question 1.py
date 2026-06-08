import yfinance as yf
import pandas as pd

tickers = ['1155.KL', '1295.KL', '5347.KL', '1023.KL', '5225.KL']
investment_capital = 1000.00

print("Downloading fixed May-to-June historical data bracket...")

historical_data = yf.download(tickers, start='2026-05-04', end='2026-06-05')['Close']


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
    return_percentage = round((daily_return / yest_p) * 100, 2)
    
    portfolio_records.append({
        'Ticker': ticker,
        'Stock Name': stock_names[ticker],
        'Yesterday Closing Price': yest_p,
        'Today Closing Price': today_p,
        'Daily Return': daily_return,
        'Number of Shares Purchasable with RM1,000': shares_purchased,
        'Estimated Total Return': estimated_return,
        'Return Percentage': return_percentage
    })

df = pd.DataFrame(portfolio_records)

print("\n### Question 1: Main Portfolio Analysis DataFrame ###")
print(df.to_string(index=False))
print("======================================================")