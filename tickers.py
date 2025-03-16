import os
import pandas as pd

class FetchTickers:
    def __init__(self):
        self.sp500 = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks'
        self.c25 = 'https://en.wikipedia.org/wiki/OMX_Copenhagen_25#Components'

    def fetch_sp500_tickers(self):
        df = pd.read_html(self.sp500, header=0)[0]
        return(df[['Symbol', 'Security']]
               .rename(columns={'Symbol':'Ticker','Security':'Company'})
               .assign(Market='S&P 500'))

    def fetch_c25_tickers(self):
        df = pd.read_html(self.c25, header=0)[0]
        return (df[['Ticker symbol', 'Company']]
                .rename(columns={'Ticker symbol':'Ticker'})
                .assign(Market='C25')
                .assign(Ticker=lambda x: x['Ticker'].str.replace(' ', '-') + '.CO'))

    def output_tickers(self):
        sp500 = self.fetch_sp500_tickers()
        c25 = self.fetch_c25_tickers()
        df = pd.concat([sp500, c25])
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tickers.xlsx")
        df.to_excel(output_path, index=False)
        return print("Tickers has been exported.")

FetchTickers().output_tickers()