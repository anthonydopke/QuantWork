# QuantWork 📈

## Overview

**QuantWork** is a Python project for financial modeling and market data analysis.

There are currently two major development streams:
1. **Market Data** — Fetch and analyze real market data (options, stock prices, interest rates) from Yahoo Finance (or local csv/excel files)
2. **Quant Library** — Build and implement quantitative models (in progress).

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/anthonydopke/QuantWork.git
cd QuantWork
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install the project in editable mode

```bash
pip install -e .
```

This allows you to modify the source code and have the changes reflected immediately.

---

## Project Structure

```
QuantWork/
├── data_excel_csv/   
├── src/
│   ├── MarketDataLoader/
│   │   ├── OptionDataFetcher.py
│   │   └── TreasuryCurveFetcher.py
│   └── Models/     
│
├── tests/
│   └── test_import_data.ipynb
│
├── README.md
├── setup.py
└── requirements.txt
```

---

## Quick Usage Example

```python
from MarketData.OptionDataFetcher import OptionDataFetcher

# Initialize with a ticker
apple_data = OptionDataFetcher("AAPL")

# Fetch market data and build the forward curve
apple_data.build_market()

# List available maturities
print(apple_data.get_maturities())

# Plot the forward curve
apple_data.plot_forward_curve()
```

---

## Features

- ✅ Fetch stock and option chain data from Yahoo Finance
- ✅ Build interpolated forward curves
- 🚧 Work-in-progress: Quantitative models (pricing, calibration)

---

## Contributions

Feel free to fork the project and open pull requests! 🚀  
If you encounter issues or have feature requests, open a [GitHub Issue](https://github.com/anthonydopke/QuantWork/issues).

---

## Disclaimer

This project is under development and is intended for educational and research purposes only.

---

# 📢 Stay tuned for more quant tools!

