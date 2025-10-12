# ffat

Fund Fundamental Analysis Tool(FFAT) is a CLI, Python tool for fundamental analysis of funds such as mutual fund, ETFs.

Please sign this [petition on change.org]() regarding mandating disclosing fundamental metrics of funds.

## Why Use It?

When it comes to individual stocks, there are lot of metrics for fundamental analysis. When it comes to funds in India, there are only handful. And most of them like alpha, beta, Sharpe ratio **rely on past performance** of the fund. 

FFAT aims to bring those metrics to funds. It works by breaking down the individiual equity holdings of a fund, collecting metrics of individiual stock using Yfinance and then printing the median of them to stdout.
 
Currently it supports the following metrics: Forward P/E, P/E, P/B, D/E, ROE, OPM. 


## Alternative Approach using Official Portfolio Disclosure

Another way to achieve this would be to work from the official XLSX portfolio disclosure file. 

First step would be to create columns for each metric. From that a formula can be created to fetch the metric by refrencing ISIN column. Then it can be duplicated to rest of cells. From there, median and other metrics can be calculated.

This method completely avoids API calls to get fund holdings. The results are also stored in a standard format. 

However this can not be fully automated as AMCs do not adhere to a strict format when disclosing holdings. There are variations in cases, titles, formatting, colors and columns. Also none of common tools including, `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance **support querying through ISIN**. A local mapping database, or an API would be required.
