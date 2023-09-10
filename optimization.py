import yfinance as yf
import nsepython as nsep
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cvxpy as cp

assets = ['AAPL', 'MSFT', 'AMZN']
start_date = '2018-01-01'
end_date = '2023-06-01'

data = yf.download(assets, start=start_date, end=end_date)['Adj Close']

returns = data.pct_change().dropna()

# Plotting the price movements
plt.figure(figsize=(10, 6))
for asset in assets:
    plt.plot(data.index, data[asset], label=asset)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Movements')
plt.legend()

plt.show()


# Calculating daily returns
returns = data.pct_change().dropna()

# Plotting the distribution of returns
plt.figure(figsize=(10, 6))
for asset in assets:
    plt.hist(returns[asset], bins=50, alpha=0.5, label=asset)

plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.title('Distribution of Daily Returns')
plt.legend()

plt.show()



# Number of assets
n_assets = len(assets)

# Allocation weights variable
weights = cp.Variable(n_assets)

# Constraints
constraints = [
    weights >= 0,
    cp.sum(weights) == 1
]

# Expected return
expected_return = cp.sum(cp.multiply(returns.mean(), weights))

# Portfolio variance
portfolio_variance = cp.quad_form(weights, returns.cov())

# Objective function
objective = cp.Maximize(expected_return - 0.5 * portfolio_variance)


# Solve the optimization problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Optimal allocation weights
optimal_weights = weights.value

# Expected return of the portfolio
portfolio_return = np.dot(returns.mean(), optimal_weights)

# Risk (standard deviation) of the portfolio
portfolio_risk = np.sqrt(np.dot(optimal_weights.T, np.dot(returns.cov(), optimal_weights)))

# Sharpe ratio of the portfolio
risk_free_rate = 0.02  # Assuming a risk-free rate of 2%
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk

print(f"Expected Return: {portfolio_return:.2%}")
print(f"Risk (Standard Deviation): {portfolio_risk:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Pie chart of portfolio allocation
plt.figure(figsize=(8, 8))
plt.pie(optimal_weights, labels=assets, autopct='%1.1f%%')
plt.title('Portfolio Allocation')

plt.show()
