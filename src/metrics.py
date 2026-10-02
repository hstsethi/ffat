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



def get_metrics(fund_holdings: list[str], metric: str) -> list:
    tickers = yf.Tickers(" ".join(fund_holdings)) # Initialize all tickers at once instead of looping
    metrics = [
        tickers.tickers[ticker].info.get(metric)
        for ticker in fund_holdings
    ]
    return metrics 

