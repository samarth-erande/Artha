"""
Artha - Data Storage

Purpose:
    Store validated stock market data on disk.

Responsibilities:
    - Save validated data.
    - Generate standardized filenames.
    - Return the saved file path.

This module does NOT:
    - Download data.
    - Validate data.
    - Clean data.
    - Perform analysis.
"""

from pathlib import Path
import pandas as pd


def save_raw_data(data: pd.DataFrame,ticker: str,) -> Path:

    output_directory = Path("data/raw") #For safety , here we assume file does not exist
    output_directory.mkdir(parents=True, exist_ok=True)

    filename = f"{ticker.replace('.', '_')}.csv" #for clean and standard format

    output_path = output_directory / filename

    data.to_csv(output_path)

    return output_path        