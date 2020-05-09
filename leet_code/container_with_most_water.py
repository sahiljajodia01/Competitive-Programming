# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/830/

###### Two pointer approach #######
class Solution:
    def maxArea(self, height: List[int]) -> int:
        count1 = 0
        count2 = len(height)-1
        max_ = 0
        while count1 < count2:
            area = (min(height[count1], height[count2]) * (count2 - count1))
            
            if area > max_:
                max_ = area
            
            if height[count1] <= height[count2]:
                count1 += 1
            else:
                count2 -= 1
        
        return max_