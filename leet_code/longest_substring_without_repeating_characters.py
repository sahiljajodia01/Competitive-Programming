# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/


######### My solution. Accepted. Time complexity mostly linear #########
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_length = 0
        length = 0
        for i in range(len(s)):
            if s[i] not in d.keys() or d[s[i]] == 0:
                d[s[i]] = 1
                length += 1
            else:
                decrease = 0
                for j in range(i-length, i):
                    if s[j] == s[i]:
                        d[s[j]] -= 1
                        decrease += 1
                        break
                    
                    d[s[j]] -= 1
                    decrease += 1
                length -= decrease
                d[s[i]] += 1
                length += 1
        
            if length > max_length:
                max_length = length

        return max_length