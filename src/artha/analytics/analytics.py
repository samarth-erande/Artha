"""
Artha - Financial Analytics

Purpose:
    Calculate basic financial metrics from processed
    stock market data.

Responsibilities:
    - Calculate daily returns.
    - Calculate cumulative returns.
    - Calculate price statistics.
    - Calculate volume statistics.
    - Calculate volatility.

This module does NOT:
    - Download data.
    - Validate data.
    - Clean data.
    - Store data.
    - Train machine learning models.
"""

import pandas as pd


def calculate_metrics(data: pd.DataFrame) -> dict:


    daily_returns = data["Close"].pct_change()

    cumulative_return = (1 + daily_returns).prod() - 1

    price_statistics = data["Close"].describe()

    volume_statistics = data["Volume"].describe()

    volatility = daily_returns.std()

    running_max = data["Close"].cummax()

    drawdown = (data["Close"] - running_max) / running_max

    maximum_drawdown = drawdown.min()

    return {
        "daily_returns": daily_returns,
        "cumulative_return": cumulative_return,
        "price_statistics": price_statistics,
        "volume_statistics": volume_statistics,
        "volatility": volatility,
        "drawdown": drawdown,
        "maximum_drawdown": maximum_drawdown,
    }