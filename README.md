# Nighteye

## Introduction

We have created a model for cryptocurrencies perdictions namely, Bitcoin, Ethereum, Cardano, Solana, Polygon based on last 15 day's
closing price.

## Dataset and Preprocessing

We collected data using yfinance API. Data is dated from each coin's listing to 20th December 2021. Our model takes input of past 15 days and predict the price of the next data. We collected each day's high, low, opening, closing and number of volumn traded.

### Preprocessing

We worked with only the closing price of the coin. After dropping all the columns other than `close`, we then applied normalization on the closing price.

## Model

We have created a sequential model of 3 LSTM layers and a Dense layer which will help to predict the price.
We have used Adam optimizer with learning rate of 0.001. And Mean Squared Error as loss function.
Then we have trained the model for 100 epochs with batch size of 64 and validation split of 0.1.

## Predictions

Live prediction use CoinMarketCap API to collect last 15 days data to predict the closing price of the coin.

You can check it out [here](http://20.204.220.26/)
