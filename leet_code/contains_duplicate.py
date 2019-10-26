# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

########## Using sorting (nlogn) without extra memory #############
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) <= 1:
#             return False
        
#         nums_in_order = sorted(nums)
#         print(nums_in_order)
#         prev = nums_in_order[0]
#         for i in range(1, len(nums_in_order)):
#             if nums_in_order[i] == prev:
#                 return True
#             else:
#                 prev = nums_in_order[i]
                
        
#         return False



######### Another solution using hashmaps with time complexity (n) but space complexity also (n) #########
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) <= 1:
#             return False
        
#         d = {}
        
#         for i in range(len(nums)):
#             if nums[i] in d.keys():
#                 d[nums[i]] += 1
#             else:
#                 d[nums[i]] = 1
                
#         for key, value in d.items():
#             if value > 1:
#                 return True
        
#         return False