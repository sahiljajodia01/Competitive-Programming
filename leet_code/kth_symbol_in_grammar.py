# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/


####### My solution. Works for N upto 25. But fails for N > 25.
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        dp = ['0', '1']
        
        def solve(dp, index, N):
            if index > N:
                return dp
            
            dp += dp[(2**(index-2)//2):] + dp[:(2**(index-2)//2)]
                
            return solve(dp, index+1, N)
        
        dp = solve(dp, 3, N)
        
        return int(''.join(dp)[K-1])


###### Solution I read in discussion. It works for all cases of N.
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def solve(N, K):
            if N == 1:
                return 0

            if K % 2 == 0:
                if solve(N-1, K//2) == 0:
                    return 1
                else:
                    return 0
            else:
                if solve(N-1, (K+1)//2) == 0:
                    return 0
                else:
                    return 1
        
        return solve(N, K)