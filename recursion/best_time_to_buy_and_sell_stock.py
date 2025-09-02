#122 Best time to buy and sell stock

def maxProfit(prices: list[int]) -> int:
    memo = {}
    def getMax(day: int, stock: int) -> int:
        
        ## Base case
        if day == len(prices):
            return 0
        
        ## Caching
        if (day, stock) in memo:
            return memo[(day, stock)]

        if stock == 1:
            # We can either sell the stock or hold
            sell = prices[day] + getMax(day + 1, 0)
            hold = getMax(day + 1, 1)
            profit = max(sell, hold)
            memo[(day, stock)] = profit
            return profit
        else:
            # We can either buy the stock or skip
            buy = -prices[day] + getMax(day + 1, 1)
            skip = getMax(day + 1, 0)
            profit = max(buy, skip)
            memo[(day, stock)] = profit
            return profit

    return getMax(0, 0)


print(maxProfit([7,1,5,3,6,4])) # 7