# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/


# A top down dynamic programming solution for the problem
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(-1)
            arr.append(temp)
            
        # arr = [[-1 for i in range(n)] for i in range(m)]
        def solve(m, n, arr):
            # print(n, m)
            # print(arr)
            if arr[n][m] > 0:
                return arr[n][m]
            elif m == 0 or n == 0:
                return 1
            else:
                arr[n][m] = solve(m-1, n, arr) + solve(m, n-1, arr)
                return arr[n][m]
        
        return solve(m-1, n-1, arr)