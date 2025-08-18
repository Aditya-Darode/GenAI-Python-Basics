'''You are given an array prices where prices[i] represents the stock price on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a later day to sell that stock.
Return the maximum profit you can achieve from this transaction.
If no profit is possible (prices keep falling), return 0.'''


def maxProfit(prices):

    # Initialize min_price with a very large number (infinity-like)
    # This will store the lowest price we have seen so far (best buy day).
    min_price = 9999999

    # Initialize max_profit as 0 because profit cannot be negative
    max_profit = 0

    for price in prices:

        # If today's price is cheaper than all previous ones,
        # update min_price (better day to buy)
        if price < min_price:
            min_price = price
        else:
            # Otherwise, calculate the profit if we sold today
            profit = price - min_price

            # If today's profit is greater than the best profit so far,
            # update max_profit
            if profit > max_profit:
                max_profit = profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
