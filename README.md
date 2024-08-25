# Portafolio_Crypto2024
Este repositorio contiene un análisis detallado de un portafolio compuesto por criptomonedas y bonos, utilizando datos históricos y siendo implementado en 2024. Se evalua el desempeño y el riesgo del portafolio.

# Portafolio_Crypto2024
Este repositorio contiene un análisis detallado de un portafolio compuesto por criptomonedas y bonos, utilizando datos históricos y siendo implementado en 2024. Se evalua el desempeño y el riesgo del portafolio.

## Estructura del Proyecto

El proyecto está compuesto por tres scripts principales:

### 1. `Portafolio_crypto2024.py`

Este script se encarga de la configuración y manejo del portafolio de criptomonedas. A continuación se describen los detalles específicos:

#### **Criptomonedas Utilizadas**
Las criptomonedas seleccionadas para este portafolio son:
- **XRP-USD (Ripple)**
- **SOL-USD (Solana)**
- **ETH-USD (Ethereum)**
- **DOGE-USD (Dogecoin)**
- **BNB-USD (Binance Coin)**
- **CHZ-USD (Chiliz)**

Estas criptomonedas fueron elegidas debido a su alta capitalización de mercado y volatilidad, lo que permite capturar una amplia gama de comportamientos en el mercado de criptomonedas.

#### **Asignación de Pesos**
El portafolio se distribuye de la siguiente manera:
- **XRP-USD:** 4.67%
- **SOL-USD:** 20%
- **ETH-USD:** 4.67%
- **DOGE-USD:** 5%
- **BNB-USD:** 4.67%
- **CHZ-USD:** 5%
- **AGG (iShares Core U.S. Aggregate Bond ETF):** 20%
- **TLT (iShares 20+ Year Treasury Bond ETF):** 20%
- **LQD (iShares iBoxx $ Investment Grade Corporate Bond ETF):** 10%

La inclusión de ETFs de bonos como **AGG**, **TLT**, y **LQD** busca proporcionar estabilidad al portafolio, compensando la alta volatilidad de las criptomonedas con activos de menor riesgo.

#### **Obtención de Datos Históricos**
Utilizamos la biblioteca `yfinance` para descargar datos históricos de precios ajustados desde Yahoo Finance. Los datos cubren un período desde el 1 de enero de 2018 hasta el 31 de agosto de 2023.

#### **Cálculo de Retornos**
Se calculan los retornos porcentuales diarios y mensuales de cada activo en el portafolio. Estos retornos son fundamentales para los análisis posteriores, como el backtesting y la simulación de escenarios.

### 2. `Backtest.py`

Este script realiza un backtesting del portafolio, lo que permite analizar cómo habría funcionado en el pasado bajo las condiciones históricas. Los detalles de este proceso son los siguientes:

#### **Simulación de Rendimiento Histórico**
El rendimiento del portafolio se simula utilizando los datos históricos descargados previamente. Esto incluye:
- **Rendimientos Diarios:** Se calculan los rendimientos diarios para evaluar la volatilidad y el comportamiento a corto plazo.
- **Rendimientos Mensuales:** Se analizan los rendimientos mensuales para capturar tendencias a mediano plazo.

#### **Cálculo de Métricas de Rendimiento**
Se calculan varias métricas clave para evaluar el rendimiento del portafolio:
- **Retorno Anualizado:** Calcula el retorno promedio anual basado en los datos históricos.
- **Volatilidad Anualizada:** Mide la desviación estándar de los rendimientos anuales, proporcionando una idea de la variabilidad del portafolio.
- **Value at Risk (VaR):** Estima la posible pérdida máxima en un período específico con un nivel de confianza dado.
- **Ratio de Sharpe:** Mide el rendimiento ajustado al riesgo del portafolio, comparando el retorno del portafolio con la tasa libre de riesgo.

#### **Visualización**
Se grafica la evolución del valor del portafolio a lo largo del tiempo, lo que permite visualizar cómo ha cambiado el valor del portafolio durante el período analizado. Esta gráfica es útil para identificar patrones y ciclos en los datos históricos.

### 3. `Scenarios.py`

Este es el script más importante del proyecto, encargado de crear diferentes escenarios futuros considerando a BTC como el benchmark. A continuación se detallan las razones y el proceso detrás de esta elección:

#### **Razón para Usar BTC como Benchmark**
Bitcoin (BTC) es la criptomoneda más grande y reconocida en el mercado, y a menudo se considera un barómetro del rendimiento general del mercado de criptomonedas. Debido a su alta capitalización y liquidez, BTC se utiliza como benchmark para medir el comportamiento relativo de otras criptomonedas. Las betas de las demás criptomonedas se calculan en relación con BTC para capturar su sensibilidad a los movimientos del mercado.

#### **Cálculo de Betas**
Se calculan las betas de cada criptomoneda en relación con BTC utilizando datos históricos de retornos mensuales. La beta mide la sensibilidad de una criptomoneda a los movimientos de BTC. Una beta mayor a 1 indica que la criptomoneda es más volátil que BTC, mientras que una beta menor a 1 indica menor volatilidad.

#### **Definición de Escenarios**
Se crean tres escenarios principales:
- **Optimista:** BTC tiene un rendimiento superior al promedio, sugiriendo un mercado alcista.
- **Neutral:** BTC tiene un rendimiento promedio, reflejando condiciones de mercado estables.
- **Pesimista:** BTC tiene un rendimiento inferior al promedio, indicando un mercado bajista.

#### **Simulación de Rendimiento Futuro**
Se simula el rendimiento mensual del portafolio durante un año bajo cada uno de los escenarios. La simulación incluye:
- **Retornos Simulados de Criptomonedas:** Se generan utilizando las betas calculadas y la volatilidad histórica.
- **Retornos Simulados de Fondos:** Basados en sus medias y volatilidades históricas.

#### **Visualización**
Se grafica la trayectoria mensual acumulativa del portafolio bajo los diferentes escenarios. Esto permite una fácil comparación de cómo podría evolucionar el portafolio en condiciones de mercado variables. Las gráficas incluyen:
- **Trayectoria del Portafolio en Escenario Optimista**
- **Trayectoria del Portafolio en Escenario Neutral**
- **Trayectoria del Portafolio en Escenario Pesimista**



## Instalación y Configuración

### Requisitos
- Python 3.7 o superior
- Bibliotecas Python necesarias:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`

### Instalación de Bibliotecas
Puedes instalar las bibliotecas necesarias ejecutando el siguiente comando:

```bash
pip install yfinance pandas numpy matplotlib seaborn
