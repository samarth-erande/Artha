"""
Artha - Stock Market Data Downloader

Purpose:
    Download historical stock market data from Yahoo Finance.

Responsibilities:
    - Download historical data.
    - Return a Pandas DataFrame.
    - Raise meaningful exceptions on failure.

This module does NOT:
    - Validate data.
    - Save data.
    - Perform analysis.
"""

from datetime import date

import pandas as pd
import yfinance as yf


def download_stock_data(
    ticker: str,
    start_date: date,
    end_date: date,
) -> pd.DataFrame:
    """
    Download historical stock market data for a ticker.

    Parameters
    ----------
    ticker : str
        Stock ticker (e.g. RELIANCE.NS)

    start_date : date
        Start date of historical data.

    end_date : date
        End date of historical data.

    Returns
    -------
    pd.DataFrame
        Historical OHLCV market data.

    Raises
    ------
    ValueError
        If no data is returned.

    RuntimeError
        If Yahoo Finance cannot provide data.
    """

    try:
        data = yf.download(
            tickers=ticker,
            start=start_date.isoformat(),
            end=end_date.isoformat(),
            progress=False,
        )

    except Exception as exc:
        raise RuntimeError(
            f"Failed to download data for '{ticker}'."
        ) from exc

    if data.empty:
        raise ValueError(
            f"No historical data found for '{ticker}'."
        )

    return data