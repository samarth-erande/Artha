"""
Artha - Statistical Visualization

Purpose:
    Create statistical visualizations for financial data.

Responsibilities:
    - Plot return distributions.
    - Plot price distributions.
    - Plot volume distributions.
    - Plot correlation heatmaps.

This module does NOT:
    - Download data.
    - Validate data.
    - Clean data.
    - Calculate financial metrics.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_return_distribution(daily_returns: pd.Series,):


    figure, axis = plt.subplots(figsize=(10, 6))

    sns.histplot(daily_returns.dropna(),kde=True,ax=axis)

    axis.set_title("Daily Return Distribution")
    axis.set_xlabel("Daily Return")
    axis.set_ylabel("Frequency")
    axis.grid(True)

    figure.tight_layout()

    return figure


def plot_price_distribution(data: pd.DataFrame):

    figure, axis = plt.subplots(figsize=(10, 6),)

    sns.histplot(data["Close"],kde=True,ax=axis)

    axis.set_title("Closing Price Distribution")
    axis.set_xlabel("Closing Price")
    axis.set_ylabel("Frequency")
    axis.grid(True)

    figure.tight_layout()

    return figure


def plot_volume_distribution(data: pd.DataFrame):

    figure, axis = plt.subplots(figsize=(10, 6))

    sns.histplot(data["Volume"], kde=True,ax=axis)

    axis.set_title("Trading Volume Distribution")
    axis.set_xlabel("Volume")
    axis.set_ylabel("Frequency")
    axis.grid(True)

    figure.tight_layout()

    return figure


def plot_correlation_heatmap(data: pd.DataFrame):

    columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    correlation = data[columns].corr()

    figure, axis = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=axis,
    )

    axis.set_title("OHLCV Correlation Heatmap")

    figure.tight_layout()

    return figure