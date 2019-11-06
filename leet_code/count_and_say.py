# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/

# class Solution:
#     def countAndSay(self, n: int) -> str:
#         count = 1
#         number = 0
#         initial = "1"
#         ans = ""
#         while n > 1:
#             first = initial[0]
#             for i in range(1, len(initial)):
#                 if initial[i] == first:
#                     count += 1
#                 else:
#                     ans += str(count)
#                     ans += first
#                     count = 1
#                     first = initial[i]
            
#             ans += str(count)
#             ans += first
#             count = 1
#             initial = ans
#             ans = ""
#             n -= 1
        
#         return initial