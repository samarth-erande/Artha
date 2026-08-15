# Product Requirements Document (PRD)

**Project:** Artha  
**Version:** 0.1.0

---

# Objective

Build a modular financial data platform for the Indian stock market with production-quality engineering practices.

---

# Completed Milestones

## Repository Foundation
- Repository initialized
- Standard project structure
- Bootstrap automation
- GitHub integration

---

## Data Ingestion

Status: ✅ Complete

Features:
- Historical stock download
- Yahoo Finance integration
- Exception handling
- Type-safe API

---

## Data Validation

Status: ✅ Complete

Features:
- Empty DataFrame validation
- DatetimeIndex validation
- Required column validation
- Duplicate index detection
- Empty row detection

---
Status: ✅ Complete

Features:
- Save validated stock market data.
- Automatic raw data directory creation.
- Standardized CSV file generation.
- Standardized filename generation from ticker symbols.
- Return saved file path for downstream use.

---

## Data Processing

Status: ✅ Complete

Features:
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
- Save processed datasets.

---

## Financial Analytics

Status: ✅ Complete

Features:
- Calculate daily returns.
- Calculate cumulative returns.
- Calculate price statistics.
- Calculate volume statistics.
- Calculate volatility.
- Calculate drawdown.
- Calculate maximum drawdown.
- Calculate rolling mean with configurable window size.
- Calculate rolling volatility with configurable window size.