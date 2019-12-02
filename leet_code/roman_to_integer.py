# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        initial_val = 0
        for i in range(len(s)-1, -1, -1):
            if d[s[i]] >= initial_val:
                ans += d[s[i]]
            else:
                ans -= d[s[i]]
                
            initial_val = d[s[i]]
            
        return ans