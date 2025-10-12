# ffat

Fund Fundamental Analysis Tool(FFAT) is a CLI, Python tool for fundamental analysis of funds such as mutual fund, ETFs.

Please sign this [petition on change.org]() regarding mandating disclosing fundamental metrics of funds.

## Why Use It?

When it comes to individual stocks, there are lot of metrics for fundamental analysis. When it comes to funds in India, there are only handful. And most of them like alpha, beta, Sharpe ratio **rely on past performance** of the fund. 

FFAT aims to bring those metrics to funds. It works by breaking down the individiual equity holdings of a fund, collecting individiual stock metrics using Yfinance and then returning the median of them to stdout.
 
Currently it supports the following metrics: Forward P/E, P/E, P/B, D/E, ROE, OPM. 


## Alternative Approach using Official Portfolio Disclosure

Another way to achieve this would be to work from the official XLSX portfolio disclosure file. 

First step would be to create columns for each metric. From that a formula can be created to fetch the metric by refrencing ISIN column. Then it can be duplicated to rest of cells. From there, median and other metrics can be calculated.

This method completely avoids API calls to get fund holdings. The results are also stored in a standard format. However none of common tools including, `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance **support querying through ISIN**.
