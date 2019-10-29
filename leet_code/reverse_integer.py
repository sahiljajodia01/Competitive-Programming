# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

# class Solution:
#     def reverse(self, x: int) -> int:
        
#         rev_num = 0
#         copy = abs(x)
#         while copy != 0:
#             digit = copy % 10
#             rev_num = rev_num * 10 + digit
#             copy = copy//10
#         if rev_num >= 2147483648:
#             return 0
#         else:
#             if x >= 0:
#                 return rev_num
#             else:
#                 return rev_num * -1