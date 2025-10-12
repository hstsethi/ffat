# ffat
Fund Fundamental Analysis Tool(FFAT) is a CLI, Python tool for fundamental analysis of funds such as mutual fund, ETFs.

## Why Use It?

When it comes to individual stocks, there are lot of metrics for fundamental analysis. When it comes to funds in India[^1], there are only handful. And most of them like alpha, beta, Sharpe ratio **rely on past performance.**

FFAT aims to bring those metrics to funds. It works by breaking down the individiual equity holdings of fund, collecting their metrics and then returning the median of them to stdout.
 
Currently it supports the following metrics: Forward P/E, P/E, P/B, D/E, ROE, OPM. 

1: Many US funds provide this information. For example, see [VOO's Portfolio Composition section](https://investor.vanguard.com/investment-products/etfs/profile/voo#portfolio-composition).

## Alternative Approach using Spreadsheets

Another way to achieve this would be to work from the official XLSX disclosure file. 

First step would be to create columns for each metric. From that a formula can be created to fetch the metric by refrencing ISIN column. Then it can be duplicated to rest of cells. From there, median and other metrics can be calculated.

This method completely avoids API calls to get fund holdings. The results are also stored in machine redable format. But it can not be feasibly automated, and GOOGLEFINANCE function in Google Sheets **does not support querying through ISIN**.
