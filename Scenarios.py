import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Configuración de estilo para los gráficos
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

# Establecer una semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

# Definición de los tickers
crypto_tickers = ['XRP-USD', 'SOL-USD', 'ETH-USD', 'DOGE-USD', 'BNB-USD', 'CHZ-USD']
benchmark_ticker = 'BTC-USD'
fund_tickers = ['AGG', 'TLT', 'LQD']

# Definición de pesos del portafolio
weights = {
    'XRP-USD': 0.0467,
    'SOL-USD': 0.20,
    'ETH-USD': 0.0467,
    'DOGE-USD': 0.05,
    'BNB-USD': 0.0467,
    'CHZ-USD': 0.05,
    'AGG': 0.20,
    'TLT': 0.20,
    'LQD': 0.10
}

# Descarga de datos desde Yahoo Finance
data = yf.download(crypto_tickers + [benchmark_ticker] + fund_tickers, 
                   start="2018-01-01", 
                   end="2023-08-31", 
                   progress=False)['Adj Close']

# Cálculo de retornos mensuales
monthly_prices = data.resample('M').last()
monthly_returns = monthly_prices.pct_change().dropna()

# Separación de retornos por tipo de activo
crypto_returns = monthly_returns[crypto_tickers]
benchmark_returns = monthly_returns[benchmark_ticker]
fund_returns = monthly_returns[fund_tickers]

# Cálculo de Betas de las Criptomonedas respecto a BTC
betas = {}
for crypto in crypto_tickers:
    covariance = np.cov(crypto_returns[crypto], benchmark_returns)[0][1]
    variance = np.var(benchmark_returns)
    beta = covariance / variance
    betas[crypto] = beta

betas_df = pd.DataFrame.from_dict(betas, orient='index', columns=['Beta'])
print("Betas de las Criptomonedas respecto a BTC:")
print(betas_df)  # Reemplazado display() por print()

# Definición de Escenarios
btc_mean = benchmark_returns.mean()
btc_std = benchmark_returns.std()

btc_scenarios = {
    'Optimista': btc_mean + btc_std,
    'Neutral': btc_mean,
    'Pesimista': btc_mean - btc_std
}

# Simulación de Retornos Mensuales del Portafolio
simulation_periods = 12  # 12 meses

scenario_portfolio_values = {}

for scenario_name, btc_expected_return in btc_scenarios.items():
    portfolio_values = [1]  # Empezamos con un valor de portafolio de 1 (100%)
    
    for month in range(simulation_periods):
        btc_return = np.random.normal(loc=btc_expected_return, scale=btc_std)
        
        # Simulación de retornos de criptomonedas basados en la beta y volatilidad histórica
        crypto_simulated_returns = {}
        for crypto in crypto_tickers:
            crypto_volatility = crypto_returns[crypto].std()
            crypto_return = betas[crypto] * btc_return + np.random.normal(0, crypto_volatility)
            crypto_simulated_returns[crypto] = crypto_return
        
        # Simulación de retornos de fondos basados en volatilidad histórica
        fund_simulated_returns = {}
        for fund in fund_tickers:
            fund_mean_return = fund_returns[fund].mean()
            fund_volatility = fund_returns[fund].std()
            fund_return = np.random.normal(loc=fund_mean_return, scale=fund_volatility)
            fund_simulated_returns[fund] = fund_return
        
        # Cálculo del retorno total del portafolio para el mes actual
        total_return = sum(weights[asset] * (crypto_simulated_returns.get(asset, 0) + fund_simulated_returns.get(asset, 0)) 
                           for asset in weights.keys())
        
        # Actualización del valor del portafolio
        new_portfolio_value = portfolio_values[-1] * (1 + total_return)
        portfolio_values.append(new_portfolio_value)
    
    # Almacenamiento de los valores del portafolio para el escenario actual
    scenario_portfolio_values[scenario_name] = portfolio_values

# Creación de DataFrame con los resultados de los escenarios
results_df = pd.DataFrame(scenario_portfolio_values)
results_df.index = pd.date_range(start='2023-09-01', periods=simulation_periods + 1, freq='M')

# Visualización de los Resultados
plt.figure(figsize=(14, 8))

for scenario in results_df.columns:
    plt.plot(results_df.index, (results_df[scenario] - 1) * 100, marker='o', label=scenario)

plt.title('Trayectorias Mensuales Acumulativas del Portafolio Bajo Diferentes Escenarios')
plt.xlabel('Mes')
plt.ylabel('Retorno Acumulado (%)')
plt.legend(title='Escenarios')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
