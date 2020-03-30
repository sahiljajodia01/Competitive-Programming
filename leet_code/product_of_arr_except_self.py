# https://leetcode.com/problems/product-of-array-except-self/

######## A O(n) and linear space solution. I had to look at the solution for this problem ########
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(left)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(len(right)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        ans = [1] * len(nums)
        
        for i in range(len(ans)):
            ans[i] = left[i] * right[i]
        
        return ans


####### A O(n) time but constant space solution. #######
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        for i in range(len(ans)-2, -1, -1):
            ans[i] = ans[i+1] * nums[i+1]
        
        left_prod = 1
        for i in range(1, len(nums)):
            left_prod = left_prod * nums[i-1]
            ans[i] = left_prod * ans[i]
            
        return ans