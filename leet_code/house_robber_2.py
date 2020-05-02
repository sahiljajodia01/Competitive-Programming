# https://leetcode.com/problems/house-robber-ii/


######## I did not get this solution by myself. I had to look this in discussions
class Solution:
    def rob(self, nums: List[int]) -> int:    
        def solve(nums, end, arr):
            # if end < 0:
            #     return 0
            if arr[end] != -1:
                return arr[end]
            else:
                first = nums[end] + solve(nums, (end-2), arr)
                second = solve(nums, (end-1), arr)
                arr[end] = max(first, second)
                return arr[end]
        

        if nums == []:
            return 0
    
        if len(nums) <= 2:
            return max(nums)
        
        arr = [-1] * len(nums)
        arr[0] = 0
        arr[1] = nums[1]
        
        ans1 = solve(nums, len(nums)-1, arr)
        
        arr = [-1] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])
        
        ans2 = solve(nums, len(nums)-2, arr)
                
        return max(ans1, ans2)