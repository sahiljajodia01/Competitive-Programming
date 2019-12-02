# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/


######### A very naive solution ###########
####### There are a lot of other methods to solve this problem. I should revisit those methods again later. ############
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 3
        if n == 1:
            return True
        while i <= n:
            if i == n:
                return True
            
            i *= 3
            
        return False