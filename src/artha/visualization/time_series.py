"""
Artha - Time-Series Visualization

Purpose:
    Create time-series visualizations for financial analysis.

Responsibilities:
    - Plot cumulative returns.
    - Plot rolling mean.
    - Plot rolling volatility.
    - Plot drawdown over time.

This module does NOT:
    - Download data.
    - Validate data.
    - Clean data.
    - Calculate financial metrics.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_cumulative_return(daily_returns: pd.Series):

    cumulative_return = (1 + daily_returns).cumprod() - 1

    figure, axis = plt.subplots(figsize=(10, 6))

    axis.plot(cumulative_return.index,cumulative_return)

    axis.set_title("Cumulative Return Over Time")
    axis.set_xlabel("Date")
    axis.set_ylabel("Cumulative Return")
    axis.grid(True)

    figure.tight_layout()

    return figure

def plot_rolling_mean(rolling_mean: pd.Series):

    figure, axis = plt.subplots(figsize=(10, 6))

    axis.plot(
        rolling_mean.index,
        rolling_mean,
    )

    axis.set_title("Rolling Mean Over Time")
    axis.set_xlabel("Date")
    axis.set_ylabel("Rolling Mean")
    axis.grid(True)

    figure.tight_layout()

    return figure


def plot_rolling_volatility(rolling_volatility: pd.Series):

    figure, axis = plt.subplots(
        figsize=(10, 6),
    )

    axis.plot(
        rolling_volatility.index,
        rolling_volatility,
    )

    axis.set_title("Rolling Volatility Over Time")
    axis.set_xlabel("Date")
    axis.set_ylabel("Rolling Volatility")
    axis.grid(True)

    figure.tight_layout()

    return figure


def plot_drawdown(drawdown: pd.Series):

    figure, axis = plt.subplots(figsize=(10, 6))

    axis.plot(
        drawdown.index,
        drawdown,
    )

    axis.set_title("Drawdown Over Time")
    axis.set_xlabel("Date")
    axis.set_ylabel("Drawdown")
    axis.grid(True)

    figure.tight_layout()

    return figure