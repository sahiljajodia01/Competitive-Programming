# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/

########## Recursive DP memoization solution ###########
class Solution:
    def fib(self, N: int) -> int:
        
        if N == 0:
            return 0
        dp = [-1]*(N+1)
        dp[0] = 0
        dp[1] = 1
        
        def solve(N):
            if dp[N] != -1:
                return dp[N]
            else:
                dp[N] = solve(N-1) + solve(N-2)
                return dp[N]
            
        
        return solve(N)