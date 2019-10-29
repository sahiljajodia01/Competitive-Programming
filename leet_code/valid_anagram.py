# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/

################ MY solution using two hash tables ####################
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         d_s = {}
#         d_t = {}
        
#         for i in range(len(s)):
#             if s[i] in d_s.keys():
#                 d_s[s[i]] += 1
#             else:
#                 d_s[s[i]] = 1
                
#         for i in range(len(t)):
#             if t[i] in d_t.keys():
#                 d_t[t[i]] += 1
#             else:
#                 d_t[t[i]] = 1
        
#         if len(d_s) > len(d_t):
#             outer = d_s
#             inner = d_t
#         else:
#             outer = d_t
#             inner = d_s
        
#         for key, value in outer.items():
#             if key in inner.keys():
#                 if value == inner[key]:
#                     continue
#                 else:
#                     return False
#             else:
#                 return False
            
            
#         return True



############# A more efficient solution using one hash table #################
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         d_s = {}
        
#         for i in range(len(s)):
#             if s[i] in d_s.keys():
#                 d_s[s[i]] += 1
#             else:
#                 d_s[s[i]] = 1
                
#         for i in range(len(t)):
#             if t[i] in d_s.keys():
#                 d_s[t[i]] -= 1
#             else:
#                 return False
        
#         for key, value in d_s.items():
#             if value != 0:
#                 return False
            
            
#         return True