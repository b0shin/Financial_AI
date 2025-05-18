import yfinance as yf

def fetch_yahoo_data(ticker, start, end, interval='1d'):
    data = yf.download(ticker, start=start, end=end, interval=interval)
    return data