# https://leetcode.com/problems/counting-bits/

####### A tricky bottom up DP solution. #######
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        
        total = 1
        count = 0
        for i in range(1, num+1):
            dp[i] = 1 + dp[i-total]
            count += 1
            if count == total:
                count = 0
                total *= 2
                
        
        return dp