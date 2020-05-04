# https://leetcode.com/contest/biweekly-contest-24/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

###### Pretty good recursive solution. The contraints are very small so it works perfect ######
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        sol = []
        def solve(n, arr, ans, prev, sol):
            if len(arr) == n:
                sol.append(arr)
                return
            else:
                if prev == 0:
                    solve(n, arr+ans[1], ans, 1, sol)
                    solve(n, arr+ans[2], ans, 2, sol)
                elif prev == 1:
                    solve(n, arr+ans[0], ans, 0, sol)
                    solve(n, arr+ans[2], ans, 2, sol)
                elif prev == 2:
                    solve(n, arr+ans[0], ans, 0, sol)
                    solve(n, arr+ans[1], ans, 1, sol)
            
        solve(n, "a", ["a", "b", "c"], 0, sol)
        solve(n, "b", ["a", "b", "c"], 1, sol)
        solve(n, "c", ["a", "b", "c"], 2, sol)
        print(sol)
        
        
        if k > len(sol):
            return ""
        
        return sol[k-1]