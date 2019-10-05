# https://leetcode.com/problems/license-key-formatting/
# Google

from collections import deque

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        a = S.split("-")
        a = ''.join(a)
        
        a = a.upper()
        l = deque()
        index = 0
        for i in range(len(a) - 1, -1, -K):
            if i - K < -1:
                l.appendleft(a[0:(i+1)])
            else:
                l.appendleft(a[(i+1 - K):(i+1)])
        
        l = '-'.join(l)
        
        return l