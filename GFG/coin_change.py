import pysnooper

coins = [1, 2, 3]
n = 4
m = len(coins)

@pysnooper.snoop()
def count(coins, m, n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    if m <= 0 and n > 0:
        return 0
    
    return count(coins, m-1, n) + count(coins, m, n-coins[m-1])


ans = count(coins, m, n)

print("Ans: ", ans)
