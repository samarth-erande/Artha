# Engineering Decision Records (EDR)

**Project:** Artha  
**Version:** 0.1.0  
**Status:** Active

---

# EDR-001 — Delay Adoption of pyproject.toml

## Decision
Postpone introducing `pyproject.toml` until packaging and distribution become necessary.

## Rationale
- Reduces early complexity.
- Focus on core development.
- Easier onboarding.

---

# EDR-002 — Separate Runtime and Development Dependencies

## Decision
Maintain separate dependency files:
- `requirements.txt`
- `requirements-dev.txt`

## Rationale
- Cleaner environments.
- Better dependency management.

---

# EDR-003 — Use pathlib Instead of os

## Decision
Use `pathlib` for filesystem operations.

## Rationale
- Modern Python API.
- Better readability.
- Cross-platform support.

---

# EDR-004 — Internal Date Representation

## Decision
Use `datetime.date` internally instead of strings.

## Rationale
- Type safety.
- Easier date operations.
- Clearer APIs.

---

# EDR-005 — Single Responsibility Modules

## Decision
Each module should perform exactly one responsibility.

## Rationale
- Easier testing.
- Better maintainability.
- Lower coupling.

---

# EDR-006 — Fail Fast Error Handling

## Decision
Raise meaningful exceptions immediately instead of returning invalid results.

## Rationale
- Easier debugging.
- Explicit failures.
- Reliable pipelines.

---

# EDR-007 — Abstract External Libraries

## Decision
External libraries (e.g., yfinance) must only be accessed through Artha modules.

## Rationale
- Easier provider replacement.
- Better architecture.
- Lower coupling.

---

# EDR-008 — Unified Validation Function

## Decision
Maintain a single `validate_data()` function until validation complexity justifies refactoring.

## Rationale
- Avoid premature abstraction.
- Keep validator simple.
- Refactor only when needed.

---

# EDR-009 — Immutable Raw Data Storage

## Decision

Raw market data shall remain immutable after it is downloaded and validated.

All transformations, cleaning, and feature engineering must generate new datasets instead of modifying the original raw data.

##  Rationale

- Preserves the original downloaded data.
- Enables reproducible data pipelines.
- Allows processing logic to evolve without re-downloading data.
- Simplifies debugging and recovery from processing errors.
- Aligns with industry-standard data engineering practices.

---

# EDR-010 — Data Quality Handling in Processing

## Decision

Handle data-quality issues in the Processing layer, including missing OHLCV values, exact duplicates, duplicate dates, chronological ordering, numeric type conversion, and financial-data sanity checks.

## Rationale

The Validator is responsible for structural validation, while Processing is responsible for transforming raw data into clean, analysis-ready data. Keeping these responsibilities separate prevents the validator from modifying data and ensures the raw dataset remains immutable.

---
