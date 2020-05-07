# https://leetcode.com/contest/biweekly-contest-24/problems/restore-the-array/
######## This problem is very much related to - https://leetcode.com/problems/decode-ways/ ######



######## Just took this code from there and modified it a little bit ########
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        dp = [0] * (len(s) + 1)
    
        if len(s) == 0 or s[0] == '0':
            return 0
        
        digits = 0
        temp = k
        while temp > 0:
            digits += 1
            temp = temp//10
        
        
        # for i in range(min(digits, len(dp))):
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(dp)):
            # print(dp)
            # print(1 ,s[(i-1):i], 9)
            if "0" < s[(i-1):i] <= "9":
                dp[i] += dp[i-1]
            
            count = 2
            for j in range(1, digits):
                if k < int("9"*(j+1)):
                    # print(("1" + "0" * j), s[(i-count):i], k)
                    if i - count >= 0:
                        if ("1" + "0" * j) <= s[(i-count):i] <= str(k):
                            dp[i] += dp[i-count]
                else:
                    # print(("1" + "0" * j), s[(i-count):i], ("9"*(j+1)))
                    if i - count >= 0:
                        if ("1" + "0" * j) <= s[(i-count):i] <= ("9"*(j+1)):
                            dp[i] += dp[i-count]
                count += 1
            
        
        # print(dp)
        # print('--------------------------------------------')
        
        return (dp[-1]%(1000000007))


###### I saw this solution from the discussion. This is very elegant when compared to above one ######
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [-1] * (len(s))
    
        def solve(s, k, dp, start):
            if start == len(s):
                return 1
            elif s[start] == "0":
                return 0
            elif dp[start] != -1:
                return dp[start]
            else:
                ans = 0
                res = 0
                for i in range(start, len(s)):
                    ans = (10 * ans) + int(s[i])
                    
                    if ans > k:
                        break
                    
                    res += solve(s, k, dp, i+1)
                    res = res % (1000000007)
                
                dp[start] = res
                return dp[start]
        
        return solve(s, k, dp, 0)