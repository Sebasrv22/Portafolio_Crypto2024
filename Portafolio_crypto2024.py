import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#tickers
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

# Calculate annualized return
annualized_return = portfolio_returns.mean() * 252  

# Calculate VaR using standard deviation
mean_return = portfolio_returns.mean()
std_dev_return = portfolio_returns.std()
VaR = mean_return - 1.65 * std_dev_return  

# results
print(f"Annualized Return: {annualized_return:.2%}")
print(f"VaR (using standard deviation): {VaR:.2%}")

# annualized volatility
annualized_volatility = portfolio_returns.std() * np.sqrt(252)  
print(f"Annualized Volatility: {annualized_volatility:.2%}")

# Calculate Sharpe Ratio
risk_free_rate = 0.01075  
excess_return = annualized_return - risk_free_rate
sharpe_ratio = excess_return / annualized_volatility
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")