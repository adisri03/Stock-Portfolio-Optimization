import yfinance as yf
import numpy as npy
import pandas as pd
import matplotlib.pyplot as plt
import cvxpy as cpy

assets = [] # please fill in Stock Symbol
start_date = '' # please fill in this format YYYY-MM-DD
end_date = '' # please fill in this format YYYY-MM-DD

data_set = yf.download(assets, start=start_date, end=end_date)['Adj Close']

returns = data_set.pct_change().dropna()

# Plotting the price movements
plt.figure(figsize=(10, 6))
for asset in assets:
    plt.plot(data_set.index, data_set[asset], label=asset)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Movements')
plt.legend()

plt.show()


# Calculating daily returns
returns = data_set.pct_change().dropna()

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
num_of_assets = len(assets)

# Allocation weights variable
weights = cpy.Variable(num_of_assets)

# Set the constraints
constraints = [
    weights >= 0,
    cpy.sum(weights) == 1
]

# Expected return
expected_return = cpy.sum(cpy.multiply(returns.mean(), weights))

# Portfolio variance
portfolio_variance = cpy.quad_form(weights, returns.cov())

# Objective function
objective = cpy.Maximize(expected_return - 0.5 * portfolio_variance)


# Solve the optimization problem
problem = cpy.Problem(objective, constraints)
problem.solve()

# Optimal allocation weights
optimal_weights = weights.value

# Expected return of the portfolio
portfolio_return = npy.dot(returns.mean(), optimal_weights)

# Risk (standard deviation) of the portfolio
portfolio_risk = npy.sqrt(npy.dot(optimal_weights.T, npy.dot(returns.cov(), optimal_weights)))

# Sharpe ratio of the portfolio
risk_free_rate =     # please fill in
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk

print(f"Expected Return: {portfolio_return:.2%}")
print(f"Risk (Standard Deviation): {portfolio_risk:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Pie chart of portfolio allocation
plt.figure(figsize=(8, 8))
plt.pie(optimal_weights, labels=assets, autopct='%1.1f%%')
plt.title('Portfolio Allocation')

plt.show()
