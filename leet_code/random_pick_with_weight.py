# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/


###### First cumulatively adding the weights in the array. Then finding the random number and then findin the number
###### just greater than or equal to the number using Binary Search ######
import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        
        prev = 0
        for i in range(len(self.w)):
            self.w[i] = self.w[i] + prev
            prev = self.w[i]
        
        self.maximum = self.w[-1]
        

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.maximum)
        
        left = 0
        right = len(self.w)-1
        while left < right:
            mid = (left+right)//2
            
            if self.w[mid] >= random_num:
                right = mid
            else:
                left = mid+1
        return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()