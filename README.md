# ffat
Fund Fundamental Analysis Tool(FFAT) is a CLI, Python tool for fundamental analysis of funds such as mutual fund, ETFs.

## Why Use It?

When it comes to individual stocks, there are lot of metrics for fundamental analysis. When it comes to funds in India[^1], there are only handful. And most of them like alpha, beta, Sharpe ratio **rely on past performance.**

FFAT aims to bring those metrics to funds. It works by breaking down the individiual equity holdings of fund, collecting their metrics and then calculating the median of them.  
 
Currently it supports the following metrics: Forward P/E, P/E, P/B, D/E, ROE, OPM. 

1: Many US funds provide this information. For example, see [VOO's Portfolio Composition section](https://investor.vanguard.com/investment-products/etfs/profile/voo#portfolio-composition).
