# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/

# def strStr(haystack: str, needle: str) -> int:
#     if len(needle) == 0:
#         return 0
#     elif len(needle) > len(haystack):
#         return -1
    
    
#     index = -1
#     counter = 0
#     for i in range(0, len(haystack) - len(needle) + 1):
#         if haystack[i] == needle[counter]:
#             for j in range(i, i+len(needle)):
#                 print(haystack[j], needle[counter])
#                 if haystack[j] == needle[counter]:
#                     counter += 1
#                 else:
#                     counter = 0
#                     break
#             print('---------')
#             if counter == len(needle):
#                 index = i
#                 break
            
#     return index


# ans = strStr("mississippi", "issip")

# print(ans)