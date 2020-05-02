# https://leetcode.com/problems/combination-sum-ii/

######## Backtracking solution ########
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates = sorted(candidates)
        def solve(candidates, start, target, arr, sol, total):
            # arr_sum = sum(arr)
            if total > target:
                return
            elif total == target:
                temp = arr.copy()
                if temp not in sol:
                    sol.append(temp)
            else:
                for i in range(start, len(candidates)):
                    arr.append(candidates[i])
                    solve(candidates, i+1, target, arr, sol, total+candidates[i])
                    arr.pop()
            
        
        solve(candidates, 0, target, [], sol, 0)
        return sol