# Changelog

All notable changes to this project will be documented in this file.

---

## [0.1.0] - 05-08-2026

### Added

#### Project Foundation
- Repository initialization
- Standard project structure
- Bootstrap automation
- GitHub integration

#### Data Ingestion
- Yahoo Finance downloader
- Type-safe download API
- Fail-fast error handling

#### Data Validation
- Centralized validation module
- DataFrame validation pipeline
- Structural integrity checks

### Storage
- Added raw data storage module.
- Implemented CSV persistence for validated stock market data.
- Completed end-to-end ingestion pipeline.

#### Documentation
- Initial README
- Initial PRD
- Initial Engineering Decision Records

### Data Processing

- Added processing module.
- Implemented raw-to-processed data transformation.
- Flattened MultiIndex column structure.
- Standardized processed dataset format.
### Data Processing

- Enhanced processing pipeline with data-quality handling.
- Added OHLCV numeric type conversion.
- Added missing-value handling.
- Added exact duplicate-row removal.
- Added duplicate-date detection.
- Added chronological sorting.
- Added financial-data sanity checks.
- Verified processed output through end-to-end testing.

### Financial Analytics

- Added financial analytics module.
- Implemented daily return calculation.
- Implemented cumulative return calculation.
- Implemented price statistics.
- Implemented volume statistics.
- Implemented volatility calculation.
- Added drawdown calculation.
- Added maximum drawdown calculation.
- Added rolling mean calculation.
- Added rolling volatility calculation.
- Added configurable rolling window parameter.
- Preserved expected NaN values for periods with insufficient historical observations.

### Financial Visualization v0.2.0

- Added combined financial analysis dashboard.
- Added price and moving-average visualization.
- Added volume visualization.
- Added drawdown visualization.
- Added cumulative return, volatility, and maximum drawdown summary.
- Added configurable moving-average window.

### Financial Visualization v0.3.0

- Added daily return distribution visualization.
- Added closing price distribution visualization.
- Added trading volume distribution visualization.
- Added OHLCV correlation heatmap.
- Added Seaborn-based statistical visualizations.


### Financial Visualization v0.4.0

- Added integrated statistical analysis dashboard.
- Combined return distribution, price distribution, volume distribution, and OHLCV correlation heatmap.


### Financial Visualization v0.5.0

- Added cumulative return time-series visualization.
- Added rolling mean time-series visualization.
- Added rolling volatility time-series visualization.
- Added drawdown time-series visualization.
- Integrated existing analytics outputs into time-series visualizations.
