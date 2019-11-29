# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/


################# DP memoization solution ################
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n+1)
        def solve(n, arr):
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            if arr[n] != 0:
                return arr[n]
            else:
                ones = solve(n-1, arr)
                twos = solve(n-2, arr)
                arr[n] = ones + twos
                return arr[n]
        
        
        return solve(n, arr)