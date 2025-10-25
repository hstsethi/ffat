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
    evebitda = "enterpriseToEbitda"
    fcf = "freeCashflow"


def get_metric(ticker, metric):
    # Can Initalize multiple tickers at once and return a single array
    return yf.Ticker(ticker).info.get(metric)
