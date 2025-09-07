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
    fpe = "forwardPE"

def getFundEquityHoldings(fund_id: str):
    return list(yf.Ticker(fund_id).funds_data.top_holdings.index)

def getMetric(ticker, metric):
    return yf.Ticker(ticker).info.get(metric)

def main():
    FUND_ID = "0P00005V0O.BO"
    METRIC = Metrics.pe.value # Add any value from Metrics enum
    fund_holdings = getFundEquityHoldings(FUND_ID)
    t_metrics = [getMetric(h, METRIC) for h in fund_holdings]
    t_metrics = [0 if x is None else x for x in t_metrics] # Replace None with Zero
    print("holdings: ", fund_holdings)
    print(f"median{METRIC}: {median(t_metrics)}")


if __name__ == "__main__":
    main()
