# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/


###############  This solution giving TLE #################
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         for i in range(k):
#             nums = self.rotate_once(nums)
            
            
            
#     def rotate_once(self, numbers):
#         last = numbers[-1]

#         for i in range(len(numbers)-1, 0, -1):
#             numbers[i] = numbers[i-1]

#         numbers[0] = last

#         return numbers





############## Accepted but with temparary space #############
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         temp = []
#         if k > len(nums):
#             k = k % len(nums)
        
#         for i in range(len(nums) - k, len(nums)):
#             temp.append(nums[i])
            
        
#         for i in range(len(nums) - 1, -1, -1):
#             nums[i] = nums[i - k]
            
#         for i in range(len(temp)):
#             nums[i] = temp[i]


######## There are 2 other approaches which can rotate array in place (without using extra memory) ##########