# Kentel
Kentel was a ML based AI trading tool. I started its development around July 2023 and created a fully functional product in Q2 2024. However, I needed to shut down the project due to a lack of funds.

## Structre
### Scanner
A scanner software running in the background creates AI models for every stock in the selected exchange using historical data, afterwards, the automations running in the background repeadetly goes and asks every model if it is a buy signal or a sell signal and calculates numerical possibilities. 
### Cacher
On the main server where the web platform lives, a cacher software runs in the background and gets all recent "scans" and extra data and stores it with `Redis`, it is ready to apply filters using its built-in `finviz web scraper tool`.
### Daily Insight
Kentel also offers a Daily Insight email list, depending on the user's plan. This list sends the stock picks for the day between 9:30 and 9:50 AM EST.


## Machine Learning
I spent a long time figuring out what is the best way to train the ML and asked a lot of questions about the formatting of the data. However, after all the tests I've conducted on the ML algorithms, I came to the conclusion that only candlestick+volume data was enough and it just needed to be tagged as `BUY` and `SELL`. Using the Sci-kit Learn package with python, I operated everything with `RandomForest` ML algorithm.

*Previous URL*: https://kentel.dev - offline
## Notes
- It could have grown if it was easier to use for the end user and didn't require too much trading know-how.
- Filters and timing of the data needs adjustment
- Should guide users to buy in bulk from the list instead of buying the #1 stock
