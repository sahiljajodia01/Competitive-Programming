# https://leetcode.com/problems/circle-and-rectangle-overlapping/

####### I had to look this solution in discussions
class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        
        if (x_center <= x2 and x_center >= x1) and (y_center <= y2 and x_center >= y1):
            return True
        
        if ((x_center - radius <= x1 <= x_center + radius) or (x_center - radius <= x2 <= x_center + radius)) and (y1 <= y_center <= y2):
            return True
        
        if ((y_center - radius <= y1 <= y_center + radius) or (y_center - radius <= y2 <= y_center + radius)) and (x1 <= x_center <= x2):
            return True
        
        
        points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        
        for point in points:
            dist = (x_center - point[0])**2 + (y_center - point[1])**2
            if dist <= radius**2:
                return True
        
        return False