pip install bls        #Bureau of Labor Statistics API
pip install yfinance   #Yahoo! Finance

import yfinance as yf
import datetime as dt
import bls


# Download market data from Yahoo! Finance API
# Load tickers
snp = yf.Ticker("SNP")
b = yf.Ticker('BTC-USD')
g = yf.Ticker('GC=F')

# Define start and end date for data pull
start = dt.datetime(2016,7,1)
end = dt.datetime(2021,11,30)

# Write data to csv files
sandp = yf.download('^GSPC', start, end)
sandp.to_csv("s&p_datafile.csv")

btc = yf.download('BTC-USD', start, end)
btc.to_csv('btc_datafile.csv')

gold = btc = yf.download('GC=F', start, end)
gold.to_csv('gold_datafile.csv')


# Download market data from BLS API
# Note this is monthly data

inflation = bls.get_series('CUUR0000SA0', 2016, 2021)
inflation.head()

inflation.to_csv("inf_datafile.csv")



