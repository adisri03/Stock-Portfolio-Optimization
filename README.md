# Stock-Portfolio-Optimization
![Python](https://img.shields.io/badge/Python%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)



## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Notes](#notes)

## Introduction
This script downloads historical stock price data for a user-defined list of assets and tells about how much of our portfoilio :


## Features
1. Download historical adjusted closing prices for the specified assets between a given start and end date.
2. Calculate the daily returns for each asset.
3. Plot the price movements of the selected assets over time.
4. Plot the distribution of daily returns for each asset.
5. Perform portfolio optimization to find the optimal allocation of assets that maximizes the Sharpe ratio.
6. Display key portfolio metrics such as expected return, risk (standard deviation), and Sharpe ratio.
7. Visualize the portfolio allocation using a pie chart.
## Getting Started
1. Before running the script, make sure you have installed the required libraries:
```bash
pip install yfinance nsepython numpy pandas matplotlib cvxpy
```
2. You can modify the following parameters in the script to customize your analysis:

  a. assets: A list of stock symbols to analyze.
  
  b. start_date and end_date: The date range for historical data retrieval.
  
  c. risk_free_rate: The assumed risk-free rate for calculating the Sharpe ratio. 
  
3. Run the code
   ```bash
   python portfolio_optimization.py
   ```
## Note
This script serves as a basic example of portfolio optimization and does not take into account transaction costs or constraints beyond asset weights being non-negative and summing to 1. For a real-world portfolio, consider additional factors and constraints.

Please use this script responsibly and remember that financial markets are subject to risk.



