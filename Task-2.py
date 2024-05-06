import yfinance as yf
import pandas as pd
import pandas_ta as ta
def process_ticker_data(self, ticker):
    # Download data
    data = yf.download(ticker)
    # Round all columns to 2 decimal places
    data = data.round(2)
    # Convert column names to lower case
    data.columns = data.columns.str.lower()  
    data['color'] = ['GREEN' if open <= close else 'RED' for open, close in zip(data['open'], data['close'])]
    # Calculate EMA and add as a column
    data['EMA'] = ta.ema(data['close'], length=9)
    # Save to CSV
    data.to_csv(f'{ticker}.csv', index=False)  
