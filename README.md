# CodeAlpha Stock Portfolio Tracker

A simple Python console application that calculates the value of a stock portfolio using manually defined sample prices.

## Features
- Displays five sample stock symbols and prices.
- Accepts a stock symbol and share quantity from the user.
- Calculates each holding's value and the total investment.
- Optionally saves a report to `portfolio_report.txt`.
- Validates stock symbols and quantities.

## Sample stock prices
| Symbol | Sample price (USD) |
|---|---:|
| AAPL | 180 |
| TSLA | 250 |
| GOOGL | 140 |
| MSFT | 420 |
| AMZN | 190 |

**Important:** These are hardcoded example prices for the assignment. They are not live market prices or financial advice.

## Requirements
- Python 3
- No external libraries are required.

## How to run
1. Open this folder in VS Code.
2. Open the VS Code terminal.
3. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use `py main.py`.

4. Enter stock symbols and quantities. Type `DONE` to finish.
5. Choose `yes` when asked if you want to save the report.

## Concepts used
Dictionaries, loops, functions, input/output, arithmetic and file handling.
