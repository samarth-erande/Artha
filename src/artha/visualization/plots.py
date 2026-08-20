"""
Artha - Data Visualization

Purpose:
    Create visual representations of processed and
    analytical stock market data.

Responsibilities:
    - Plot closing prices.
    - Plot trading volume.
    - Plot closing prices with rolling mean.
    - Plot drawdown.

This module does NOT:
    - Download data.
    - Validate data.
    - Clean data.
    - Calculate financial metrics.
    - Save plot files.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_price(data: pd.DataFrame):

    figure, axis = plt.subplots()

    axis.plot(data.index, data["Close"])

    axis.set_title("Closing Price")
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    axis.grid(True)

    figure.tight_layout()
    return figure


def plot_volume(data: pd.DataFrame):

    figure, axis = plt.subplots()

    axis.plot(data.index, data["Volume"])

    axis.set_title("Trading Volume")
    axis.set_xlabel("Date")
    axis.set_ylabel("Volume")
    axis.grid(True)

    figure.tight_layout()
    return figure


def plot_moving_average(data: pd.DataFrame,window: int = 20,):

    rolling_mean = data["Close"].rolling(window).mean()

    figure, axis = plt.subplots()

    axis.plot(data.index, data["Close"], label="Close")
    axis.plot(data.index, rolling_mean, label=f"{window}-Day Mean")

    axis.set_title("Closing Price and Moving Average")
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    axis.legend()
    axis.grid(True)

    figure.tight_layout()
    return figure


def plot_drawdown(drawdown: pd.Series):
    
    figure, axis = plt.subplots()

    axis.plot(drawdown.index, drawdown)

    axis.set_title("Drawdown")
    axis.set_xlabel("Date")
    axis.set_ylabel("Drawdown")
    axis.grid(True)

    figure.tight_layout()
    return figure

#Creating DashBoard
def create_financial_dashboard(data: pd.DataFrame,metrics: dict,window: int = 20,):

    rolling_mean = data["Close"].rolling(window).mean()

    figure, axes = plt.subplots(3,1,figsize=(12, 16),sharex=True)
    figure.suptitle("Artha - Financial Overview",fontsize=16,fontweight="bold",y=0.995)

    # Price + Moving Average
    axes[0].plot(data.index,data["Close"],label="Close")

    axes[0].plot(data.index,rolling_mean,label=f"{window}-Day Mean",)

    axes[0].set_title("Closing Price and Moving Average")
    axes[0].set_ylabel("Price")
    axes[0].legend()
    axes[0].grid(True)

    # Volume
    axes[1].plot(data.index,data["Volume"])

    axes[1].set_title("Trading Volume")
    axes[1].set_ylabel("Volume")
    axes[1].grid(True)

    # Drawdown
    axes[2].plot(metrics["drawdown"].index,metrics["drawdown"])

    axes[2].set_title("Drawdown")
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel("Drawdown")
    axes[2].grid(True)

    # Key Metrics
    cumulative_return = metrics["cumulative_return"]
    volatility = metrics["volatility"]
    maximum_drawdown = metrics["maximum_drawdown"]

    metrics_text = (
        f"Cumulative Return: {cumulative_return:.2%}\n"
        f"Volatility: {volatility:.2%}\n"
        f"Maximum Drawdown: {maximum_drawdown:.2%}"
    )

    figure.text(
        0.51,
        0.030,
        metrics_text,
        ha="center",
        va="bottom",
        fontsize=11,
        bbox=dict(
            boxstyle="round",
            facecolor="white",
            edgecolor="gray",
        )
    )

    figure.subplots_adjust(
        top=0.94,
        bottom=0.14,
        hspace=0.35
    )

    return figure