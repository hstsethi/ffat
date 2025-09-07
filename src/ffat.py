import yfinance as yf
from statistics import median
from enum import Enum

class Metrics(Enum):
    # Maps to keys in Yfinance .info payload
    pe = "trailingPE"
    de = "debtToEquity"
    roe = "returnOnEquity"
    pb = "priceToBook"
    opm = "operatingMargins"

def getFundEquityHoldings(fund_id: str):
    t = yf.Ticker(fund_id)
    return list(t.funds_data.top_holdings.index)

def getMetric(ticker, metric):
    return yf.Ticker(ticker).info.get(metric)

def main():
    FUND_ID = "0P00005V0O.BO"
    METRIC = Metrics.pe.value # Add any value from Metrics enum
    fund_holdings = getFundEquityHoldings(FUND_ID)
    t_metrics = [getMetric(h, METRIC) for h in fund_holdings]
    print("holdings: ", fund_holdings)
    print(f"median{metric}: {median(t_metrics)}")


if __name__ == "__main__":
    main()
