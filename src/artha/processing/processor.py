"""
Artha - Data Processing

Purpose:
    Transform raw stock market data into
    analysis-ready datasets.

Responsibilities:
    - Read raw market data.
    - Flatten MultiIndex columns.
    - Standardize column names.
    - Convert the Date index to datetime.
    - Convert OHLCV columns to numeric data types.
    - Handle missing OHLCV values.
    - Remove exact duplicate rows.
    - Reject duplicate dates.
    - Sort data chronologically.
    - Validate financial-data relationships.
    - Save processed data.

This module does NOT:
    - Download data.
    - Validate data.
    - Perform analytics.
    - Train machine learning models.
"""

from pathlib import Path

import pandas as pd

def process_raw_data(ticker: str,) -> Path:


    filename = f"{ticker.replace('.', '_')}.csv"

    raw_path = Path("data/raw") / filename
    processed_directory = Path("data/processed")
    processed_directory.mkdir(parents=True, exist_ok=True)

    processed_path = processed_directory / filename

    data = pd.read_csv(
        raw_path,
        header=[0, 1],
        index_col=0,
    )

    # Flatten MultiIndex columns
    data.columns = data.columns.get_level_values(0)

    # Standardize index
    data.index = pd.to_datetime(data.index)
    data.index.name = "Date"

    # Ensure numeric OHLCV columns
    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    data[numeric_columns] = data[numeric_columns].apply(
        pd.to_numeric,
        errors="coerce",
    )

    # Remove rows with missing OHLCV values
    data = data.dropna(subset=numeric_columns)

    # Remove exact duplicate rows
    data = data[~data.duplicated()]

    # Reject duplicate dates
    if data.index.has_duplicates:
        raise ValueError("Duplicate dates found in processed data.")

    # Sort chronologically
    data = data.sort_index()

    # Validate financial-data relationships
    invalid_prices = (
        (data["Open"] <= 0)
        | (data["High"] <= 0)
        | (data["Low"] <= 0)
        | (data["Close"] <= 0)
        | (data["Volume"] < 0)
        | (data["High"] < data["Low"])
        | (data["High"] < data["Open"])
        | (data["High"] < data["Close"])
        | (data["Low"] > data["Open"])
        | (data["Low"] > data["Close"])
    )

    if invalid_prices.any():
        raise ValueError(
            "Invalid financial values found in processed data."
        )

    data.to_csv(processed_path)

    return processed_path