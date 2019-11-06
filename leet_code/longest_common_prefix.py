# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

############### A very naive approach ##################
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         elif len(strs) == 1:
#             return strs[0]
#         ans = ""
#         counter = 0
#         flag = 0
#         while counter < len(strs[0]):
#             initial = strs[0][counter]
#             for i in range(1, len(strs)):
#                 if len(strs[i]) > counter:
#                     if strs[i][counter] == initial:
#                         continue
#                     else:
#                         flag = 1
#                         break
#                 else:
#                     flag = 1
#                     break
                    
#             if flag == 1:
#                 break
#             else:
#                 ans += initial
                
#             counter += 1
#             flag = 0
            
#         return ans