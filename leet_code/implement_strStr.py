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




############# Fast KMP string matching algorithm ##############
# def strStr(self, string: str, pattern: str) -> int:
#     pattern_seq = [0 for i in range(len(pattern))]
#     j = 0
#     i = 1
#     matched_index = -1

#     while i < len(pattern):
#         if pattern[i] == pattern[j]:
#             pattern_seq[i] = j + 1
#             i += 1
#             j += 1
#         else:
#             if j != 0:
#                 while j != 0:
#                     j = pattern_seq[j-1]
#                     if pattern[j] == pattern[i]:
#                         pattern_seq[i] = j + 1
#                         i += 1
#                         j += 1
#                         break

#                 if j == 0:
#                     pattern_seq[i] = 0
#                     i += 1
#             else:
#                 pattern_seq[i] = 0
#                 i += 1
#     # print(pattern_seq)
#     j = 0
#     i = 0
#     while i < len(string):
#         if j == len(pattern):
#             break
#         if string[i] == pattern[j]:
#             j += 1
#             i += 1
#         else:
#             if j == 0:
#                 i += 1
#                 continue
#             j = pattern_seq[j-1]

#     if j == len(pattern):
#         matched_index = i - len(pattern) 

#     return matched_index





# ans = strStr("mississippi", "issip")

# print(ans)