import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Tickers
tickers = ['XRP-USD', 'BTC-USD', 'SOL-USD', 'ETH-USD', 
           'DOGE-USD', 'BNB-USD', 'CHZ-USD', 'AGG', 'TLT', 'LQD']  

# Portfolio allocation 
weights = np.array([0.0467, 0.20, 0.0467, 0.05, 0.0467, 0.05, 0.06, 0.20, 0.20, 0.10])  

# Data
data = yf.download(tickers, start="2018-01-01", end="2024-08-21")['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change().dropna()

# Calculate weighted portfolio returns
portfolio_returns = daily_returns.dot(weights)

# Calculate cumulative returns of the portfolio
cumulative_returns = (1 + portfolio_returns).cumprod()

# Initial investment
initial_investment = 10000  

# Calculate the portfolio value over time
portfolio_value = initial_investment * cumulative_returns

# Plotting the portfolio value over time
plt.figure(figsize=(10, 6))
plt.plot(portfolio_value, label='Portfolio Value')
plt.title('Portfolio Value Over Time')
plt.xlabel('Date')
plt.ylabel('Portfolio Value (in pesos)')
plt.legend()
plt.grid(True)
plt.show()

# Displaying final portfolio value
final_value = portfolio_value[-1]
print(f"Final Portfolio Value: {final_value:.2f} pesos")
