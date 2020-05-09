# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/

####### Using two point line equation #######
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            
            eq = (x2 - x1) * (y - y1) + (y2 - y1) * (x1 - x)
            
            if eq != 0:
                return False
            
        return True