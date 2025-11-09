prices = [7,1,5,3,6,4]
max_profit = 0
buy_price = prices[0]
for i in range(1, len(prices)):
    buy_price = min(prices[i], buy_price)
    profit = prices[i] - buy_price
    max_profit = max(max_profit,profit)
print(max_profit)