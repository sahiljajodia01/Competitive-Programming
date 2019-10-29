# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         string_arr = []
        
#         for i in range(len(s)):
#             if s[i].isalnum():
#                 string_arr.append(s[i])
                
        
#         string = "".join(string_arr)
        
#         string = string.lower()
#         print(string)
#         for i in range(len(string)):
#             if string[i] != string[len(string) - i - 1]:
#                 return False    
            
#         return True