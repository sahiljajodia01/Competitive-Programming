# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/


# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
#         nums1_d = {}
        
#         for i in range(len(nums1)):
#             if nums1[i] in nums1_d.keys():
#                 nums1_d[nums1[i]] += 1
#             else:
#                 nums1_d[nums1[i]] = 1
#         ans = []
#         for i in range(len(nums2)):
#             if nums2[i] in nums1_d.keys():
#                 if nums1_d[nums2[i]] > 0:
#                     nums1_d[nums2[i]] -= 1
#                     ans.append(nums2[i])
        
#         return ans