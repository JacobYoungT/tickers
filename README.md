# Tickers Fetcher

A simple Python tool to fetch and compile stock ticker information from multiple markets.

This tool currently supports:

* S&P 500 (US market) tickers.
* OMX Copenhagen 25 (C25) tickers (with proper formatting for yfinance).

## Features

* Scrapes ticker data from Wikipedia pages.
* Formats C25 tickers with proper yfinance syntax (replaces spaces with hyphens and adds '.CO' suffix).
* Exports combined ticker data to an Excel file.

## Requirements

See `requirements.txt`.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/JacobYoungT/tickers.git
    cd tickers
    ```
   
2. Install required dependencies:

    ```bash
    pip install requirements.txt
    ```

## Usage

Simply run the script:

```bash
python tickers.py
```

The script will:

1. Fetch S&P 500 tickers from Wikipedia.
2. Fetch C25 tickers from Wikipedia and format them for yfinance.
3. Combine both datasets.
4. Export the combined data to `tickers.xlsx` in the same directory as the script.

## Output

The generated Excel file contains columns:

* Ticker: The stock ticker symbol (C25 tickers are formatted for yfinance).
* Company: The company name.
* Market: The market where the stock is listed ('S&P 500' or 'C25').

## Extending

To add support for additional markets:

1. Add the URL for the market's Wikipedia page (or other source) to the `__init__` method.
2. Create a new function to fetch and format tickers from that source.
3. Update the `output_tickers` function to include the new market's data.

## License

MIT License.