import pandas as pd
from alpha_vantage.timeseries import TimeSeries

def fetch_alpha_vantage_data(ticker, api_key, interval='1min', outputsize='compact'):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=ticker, interval=interval, outputsize=outputsize)
    return data