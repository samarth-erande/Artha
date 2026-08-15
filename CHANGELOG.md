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
