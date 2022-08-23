prices = [2,1,2,1,0,1,2]

sell = 0
for i in range(1,len(prices)):
    if prices[i] - prices[i-1] > 0:
        sell += (prices[i] - prices[i-1])
    

print(sell)