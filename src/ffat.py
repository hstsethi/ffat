from statistics import median
from metrics import *
import argparse

def getFundEquityHoldings(fund_id: str):
    return list(yf.Ticker(fund_id).funds_data.top_holdings.index)


def parse_args():
    parser = argparse.ArgumentParser(description="Require fund-id and metric.")
    parser.add_argument(
        "--fund-id",
        required=True,
        help="Fund identifier"
    )
    parser.add_argument(
        "--metric",
        # required=True,
        help="Metric name"
    )
    return parser.parse_args()
def main():
    args = parse_args()
    metric = Metrics.pe.value # Add any value from Metrics enum
    fund_holdings = getFundEquityHoldings(args.fund_id)
    t_metrics = [getMetric(h, metric) for h in fund_holdings]
    t_metrics = [0 if x is None else x for x in t_metrics] # Replace None with Zero
    print("holdings: ", fund_holdings)
    print(f"median{metric}: {median(t_metrics)}")


if __name__ == "__main__":
    main()
