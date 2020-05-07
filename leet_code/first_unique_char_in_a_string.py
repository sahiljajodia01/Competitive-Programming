# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        index_vals = []
        for key, value in d.items():
            if value == 1:
                index_vals.append(s.index(key))
        
        if len(index_vals) > 0:
            return min(index_vals)
        else:
            return -1


####### A better solution than above #######
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        
        return -1