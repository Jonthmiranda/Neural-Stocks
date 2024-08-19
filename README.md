Portuguese | [English]()

# Neural-Stocks 1.1

## Description

Study of a system for analyzing historical stock data with predictions using a neural network.

libraries: yfinance, sklearn, numpy and matplot.

## Main Features

- Download historical data of the chosen action for period x until today.
- Data analysis and stock price prediction using neural network.
- Comparison of data with graphs.

## Requirements

- Python installed
- Libraries sklearn, numpy, yfinance, matplot
- Internet access

## Installation

```bash
git clone https://github.com/Jonthmiranda/Neural-Stocks
```

## Usage

Launch financas.py using a Python IDE or CMD;

You must enter the code of the desired action, Ex: apple - AAPL, Nvidia - NVDA etc...

After you choose the code, you will search the value history in Yahoo Finance, adjust the data, analyze the data and review the results obtained, calculations and graph.

## Results obtained

- AAPL (Apple), MSFT (Microsoft), NU (Nubank) and NVDA (Nvidia) were used for testing;
- 2% error tolerance was taken into account for the results 

- APPLE
During development, AAPL was used for testing, which means Apple's actions were evaluated more times by the neural network, and of course, more accurate results

Actual values: 169.35, 143.11, 164.13...

Predicted values: 168.55, 141.63, 163.32...

R2: 0.99 (R2 goes from 0 to 1, can give a negative value, when the result is 1, it indicates a perfect model)

MAPE: 0.73 (MAPE goes from 0 to 100, the closer to 0, the more correct the model is)

Percentage of success within 2% tolerance: 96.01% (from 0% to 100%, the closer to 100%, the more identical the real values ​​and predicted values ​​are

-Microsoft:
Microsoft has been shown a few times for the model

R2: 0.99

MAPE: 0.78

Percentage: 94.52%

- Nubank
Nubank was shown the model only this time

R2: 0.99

MAP: 1.51

Percentage: 78.19%

- Nvidia
Nvidia was never shown and a longer period of value history was used

R2: 0.99

MAP: 1.95

Percentage: 58.70%

## Improvements

1.1-> Added more calculations and graph
