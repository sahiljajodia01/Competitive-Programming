# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/


####### Probably an extension of number of one bits question. ###########
######## Just counting the number of ones after taking the xor of two numbers #########
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        
        ans = bin(ans)
        
        dist = 0
        mask = 1
        for i in range(31):
            if int(ans, 2) & mask != 0:
                dist += 1
            
            mask = mask << 1
        
        return dist