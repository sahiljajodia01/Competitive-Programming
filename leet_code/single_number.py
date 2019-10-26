# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

########### Simple XOR solution with time (n) and in place (space 1) ###########
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ans = nums[0]
        
#         for i in range(1, len(nums)):
#             ans = ans ^ nums[i]
            
#         return ans


########### Other solution could be to use hashmap to store count of every number and then iterate hashmap #############
########### and return key with value 1 #############
