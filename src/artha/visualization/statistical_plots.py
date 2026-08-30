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
    - Save plot files
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

def create_statistical_dashboard(data: pd.DataFrame , daily_returns: pd.Series):

    columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    correlation = data[columns].corr()

    figure, axes = plt.subplots(2,2,figsize=(14, 10))

    figure.suptitle("Artha - Statistical Analysis",
                    fontsize=16,
                    fontweight="bold",
                    y=0.995)

    # Return Distribution
    sns.histplot(
        daily_returns.dropna(),
        kde=True,
        ax=axes[0, 0],
    )

    axes[0, 0].set_title("Daily Return Distribution")
    axes[0, 0].set_xlabel("Daily Return")
    axes[0, 0].set_ylabel("Frequency")
    axes[0, 0].grid(True)

    # Price Distribution
    sns.histplot(
        data["Close"],
        kde=True,
        ax=axes[0, 1],
    )

    axes[0, 1].set_title("Closing Price Distribution")
    axes[0, 1].set_xlabel("Closing Price")
    axes[0, 1].set_ylabel("Frequency")
    axes[0, 1].grid(True)

    # Volume Distribution
    sns.histplot(
        data["Volume"],
        kde=True,
        ax=axes[1, 0],
    )

    axes[1, 0].set_title("Trading Volume Distribution")
    axes[1, 0].set_xlabel("Volume")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].grid(True)

    # Correlation Heatmap
    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=axes[1, 1],
    )

    axes[1, 1].set_title("OHLCV Correlation Heatmap")

    figure.subplots_adjust(
        top=0.92,
        bottom=0.08,
        hspace=0.35,
        wspace=0.25,
    )

    return figure