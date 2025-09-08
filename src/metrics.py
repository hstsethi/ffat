from enum import Enum
import yfinance as yf

class Metrics(Enum):
    # Maps to keys in Yfinance .info payload
    pe = "trailingPE"
    de = "debtToEquity"
    roe = "returnOnEquity"
    pb = "priceToBook"
    opm = "operatingMargins"
    fpe = "forwardPE"

def getMetric(ticker, metric):

    return yf.Ticker(ticker).info.get(metric)


