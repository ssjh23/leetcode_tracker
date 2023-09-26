
def maxProfit(prices: List[int]) -> int:
  # Initialize maxProfit
    maxProfit = 0
  # initialize pointer of buy day
    buy = prices[0]
  # iterate through rest of the days
    for i in range(1,len(prices)):
      # Only consider the days to sell is when its more than the buy day
        if prices[i] > buy:
          # Calculate if its the best day to sell, when its tagged to the current buy day
            maxProfit = max(maxProfit,prices[i]-buy)
        else:
          # Otherwise, the best day to buy should be as small as possible
            buy = prices[i]

    return maxProfit
