# https://leetcode.com/problems/combination-sum-iv/

##### Backtracking solution #######
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        sol = []
        
        def solve(candidates, target, arr, sol):
            arr_sum = sum(arr)
            if arr_sum > target:
                return
            elif arr_sum == target:
                sol.append(1)
            else:
                for i in range(len(candidates)):
                    arr.append(candidates[i])
                    solve(candidates, target, arr, sol)
                    arr.pop()
            
        
        solve(nums, target, [], sol)
        return len(sol)


###### Faster DP solution #######
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target+1)

        def solve(nums, total, target, dp, i):
            # print(total, i)
            if total > target or i >= len(nums):
                return 0
            elif total == target:
                return 1
            elif dp[target-total] != -1:
                return dp[target-total]
            else:
                dp[target-total] = solve(nums, total+nums[i], target, dp, 0) + solve(nums, total, target, dp, i+1)
                
                return dp[target-total]
        return solve(nums, 0, target, dp, 0)