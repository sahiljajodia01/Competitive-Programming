# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = 0
        
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 count += 1
        
#         print(count)
#         while True:
#             if 0 in nums:
#                 nums.remove(0)
#             else:
#                 break
        
#         print(nums)
#         for i in range(count):
#             nums.append(0)