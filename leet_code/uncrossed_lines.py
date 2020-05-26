# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/


###### Exact LCS (Longest common substring) problem. The author just very creatively changed the problem definition ########
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = []
        for i in range(len(A)+1):
            temp = []
            for j in range(len(B)+1):
                temp.append(0)
            
            dp.append(temp)
    
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] += dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]