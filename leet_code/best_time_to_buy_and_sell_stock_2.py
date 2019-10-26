# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        initial = prices[0]
        buy = -1
        ans = 0
        sell = -1
        for i in range(1, len(prices)):
            if prices[i] > initial:
                if buy == -1:
                    buy = initial
                initial = prices[i]
            else:
                if buy == -1:
                    initial = prices[i]
                else:
                    sell = initial
                    ans += sell - buy
                    sell = -1
                    buy = -1
                    initial = prices[i]
        
        if buy != -1 and initial != buy:
            ans += initial - buy
        return ans