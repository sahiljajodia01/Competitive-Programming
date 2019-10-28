# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i in range(len(nums)):
#             if nums[i] not in d.keys():
#                 val_arr = []
#                 val_arr.append(i)
#                 d[nums[i]] = val_arr
#             else:
#                 d[nums[i]].append(i)
        
#         ans = []
#         for i in range(len(nums)):
#             temp = nums[i]
            
#             if (target - temp) in d.keys():
#                 if (target - temp) == temp:
#                     if len(d[temp]) > 1:
#                         index_1, index_2 = d[temp]
#                         ans = [index_1, index_2]
#                     else:
#                         continue
#                 else:
#                     index_1 = d[temp][0]
#                     index_2 = d[(target - temp)][0]
#                     ans = [index_1, index_2]
                
#                 break
#         return ans