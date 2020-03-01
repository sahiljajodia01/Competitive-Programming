# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# O(n^2) solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        dp = [0] * len(prices)
    
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                dp[i] = max(dp[i], prices[j]-prices[i])
        
        return max(dp)

# O(n) solution. Similar to kadane's algorithm.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        start = prices[0]
        max_ = 0
        for i in range(1, len(prices)):
            # print(start)
            if prices[i] <= start:
                if (prices[i-1] - start) > max_:
                    max_ = (prices[i-1] - start)
                start = prices[i]
            else:
                if (prices[i] - start) > max_:
                    max_ = (prices[i] - start)
        
        return max_