# ffat

Fund Fundamental Analysis Tool(FFAT) is a CLI, Python tool for fundamental analysis of funds such as mutual fund, ETFs.

Please sign this [petition on change.org](https://www.change.org/p/mandate-disclosing-fundamental-metrics-of-funds-in-monthly-disclosures) regarding mandating disclosing fundamental metrics of funds.

## Why Use It?

When it comes to individual stocks, there are lot of metrics for fundamental analysis. When it comes to funds in India, there are only handful. And most of them like alpha, beta, Sharpe ratio **rely on past performance** of the fund. 

FFAT aims to bring those metrics to funds. It works by breaking down the individiual equity holdings of a fund, collecting metrics of individiual stock using Yfinance and then printing the median of them to stdout.
 
Currently it supports the following metrics: Forward P/E, P/E, P/B, D/E, ROE, OPM. 


## Alternative Approach using Official Portfolio Disclosure

Another way to achieve this would be to work from the official portfolio disclosure document.  

This can not be fully automated as AMCs do not adhere to a strict format when disclosing portfolio holdings. There are variations in cases, titles, formatting, colors and columns, and document format. 

Manually copy relevant data from it into a different sheet and drop reduant columns. 

Use the script provided normalize column names, create columns for each metric.

Then map ISIN to symbol using [local database like in-isin-db](https://github.com/hstsethi/in-isin-db) and script provided. As none of common tools including, `=GOOGLEFINANCE`, `=STOCKHISTORY` or Yfinance **support querying through ISIN**.

From that a formula can be created to fetch the metric by refrencing the ticker column. And then it can be duplicated to rest of cells. From there, median and other metrics can be calculated.

This method completely avoids API calls to get fund holdings. The results are also stored in a standard format. 

A Google Sheets example built upon a BANKNIFTY Index Fund's XLSX, is provided in _off-disc_ directory.


