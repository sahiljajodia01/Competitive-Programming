# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/


############### This solution is a little messy with many if else conditions (possibly there could be solution with regex?) ##################
# class Solution:
#     def myAtoi(self, string: str) -> int:
#         digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
#         neg = False
#         whitespace = True
#         ans = []
#         for i in range(len(string)):
#             if string[i] == " " and whitespace == True:
#                 continue
#             else:
#                 whitespace = False
#                 if (string[i] == "-" or string[i] == '+') and len(ans) == 0:
#                     ans.append(string[i])
#                 elif string[i] in digits:
#                     ans.append(string[i])
#                 else:
#                     break

                
#         print(ans)
        
#         if len(ans) > 0:
#             if len(ans) == 1 and (ans[0] == "-" or ans[0] == "+"):
#                 return 0
#             else:
#                 ans = "".join(ans)
#                 final_int_ans = int(ans)
#                 if final_int_ans > 2147483647:
#                     return 2147483647
#                 elif final_int_ans < -2147483648:
#                     return -2147483648
#                 return final_int_ans
#         else:
#             return 0