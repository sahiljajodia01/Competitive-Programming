# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

###### I had to look this O(n) solution in discussion. I couldn't solve it myself.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_ = 0
        curr = 0
        d = {0:-1}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            
            if curr not in d.keys():
                d[curr] = i
            else:
                if (i-d[curr]) > max_:
                    max_ = (i-d[curr])
                    
        return max_