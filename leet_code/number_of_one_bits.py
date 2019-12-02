# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/

########## Now this is one solution. Another can be converting number into string and count ones char ###########
class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        ans = 0
        for i in range(32):
            if n & mask != 0:
                ans += 1
            
            mask = mask << 1
        
        return ans