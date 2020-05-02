# https://leetcode.com/problems/decode-ways/

######### I had to look this solution in the discussion
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
    
        if len(s) == 0 or s[0] == '0':
            return 0
        
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(s) + 1):
            # print(dp)
            if "0" < s[(i-1):i] <= "9":
                dp[i] = dp[i-1]
            
            if "10" <= s[(i-2):i] <= "26":
                dp[i] += dp[i-2]
        
        # print(dp)
        return dp[-1]