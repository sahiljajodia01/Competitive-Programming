# https://leetcode.com/problems/construct-k-palindrome-strings/

####### I had to look at the solution in the discussion
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d = {}
        count = 0
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            count += 1
        
        odd_count = 0
        for i in d:
            if d[i] % 2 != 0:
                odd_count += 1
        
        if len(s) < k or odd_count > k:
            return False
        else:
            return True