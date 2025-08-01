### Function to calculate maximum profit from stock prices
## This function takes a list of stock prices and calculates the maximum profit
## that can be achieved by buying and selling once.

### Max Profit Problem

def maxProfit(prices: list[int])-> int:
    min_price = float('inf')
    max_price = 0
    for price in prices:
        min_price = min(price, min_price)
        profit_or_loss = price - min_price
        max_price = max(profit_or_loss, max_price)
    return max_price

print(maxProfit(prices=[7, 1, 5, 3, 6, 4])) # Output: 5