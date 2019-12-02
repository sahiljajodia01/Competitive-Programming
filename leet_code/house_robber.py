# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/


########## Recursive memoized solution ############
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        arr = [-1] * len(nums)
        print(arr)
        def solve(nums, end, sum_, arr):
            if end < 0:
                return 0
            
            if arr[end] != -1:
                return arr[end]
            else:
                first = nums[end] + solve(nums, end-2, sum_, arr)
                second = solve(nums, end-1, sum_, arr)
                arr[end] = max(first, second)
                return arr[end]
                
        return solve(nums, len(nums)-1, 0, arr)