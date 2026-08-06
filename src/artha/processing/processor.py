"""
Artha - Data Processing

Purpose:
    Transform raw stock market data into
    analysis-ready datasets.

Responsibilities:
    - Read raw market data.
    - Flatten MultiIndex columns.
    - Standardize column names.
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

    data.columns = data.columns.get_level_values(0)
    data.index.name = "Date"

    data.to_csv(processed_path)

    return processed_path