"""
Artha - Data Validator

Purpose:
    Validate downloaded stock market data before it
    enters the processing pipeline.

Responsibilities:
    - Validate DataFrame structure.
    - Validate index.
    - Validate required columns.
    - Detect duplicate dates.
    - Detect completely empty rows.

This module does NOT:
    - Download data.
    - Clean data.
    - Save data.
    - Perform analysis.
"""

import pandas as pd

def validate_data(data: pd.DataFrame) -> None:
    """
    ValueError
        If the DataFrame fails validation.
    """

    if data.empty:
        raise ValueError("Downloaded DataFrame is empty.")

    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("DataFrame index must be a DatetimeIndex.")

    required_columns = {
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    }

    columns = set(data.columns.get_level_values(0))

    missing = required_columns - columns

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    if data.index.has_duplicates:
        raise ValueError("Duplicate dates found in index.")

    if data.isnull().all(axis=1).any():
        raise ValueError(
            "One or more rows contain only missing values."
        )