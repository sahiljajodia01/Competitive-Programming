# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/

# Very time consuming recursive solution that I came up with
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def solve(matrix, target, start_x, end_x, start_y, end_y):
            print(start_x, end_x, start_y, end_y)
            if start_x <= end_x and start_y <= end_y:
                
                mid_x = (start_x + end_x)//2
                mid_y = (start_y + end_y)//2
                
                if matrix[mid_x][mid_y] == target:
                    return True
                elif matrix[mid_x][mid_y] < target:
                    return solve(matrix, target, mid_x+1, end_x, mid_y, end_y) or solve(matrix, target, mid_x, end_x, mid_y+1, end_y) or solve(matrix, target, mid_x+1, end_x, mid_y+1, end_y)
                else:
                    return solve(matrix, target, start_x, mid_x-1, start_y, mid_y) or solve(matrix, target, start_x, mid_x, start_y, mid_y-1) or solve(matrix, target, start_x, mid_x-1, start_y, mid_y-1)
                
            return False
        
        if len(matrix) == 0:
            return False
        return solve(matrix, target, 0, len(matrix)-1, 0, len(matrix[0])-1)


# O(n+m) solution. Here we are starting from the left bottom corner elements and then comparing and finding the target element
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = 0
        i = len(matrix)-1
        
        while i >= 0 and j <= len(matrix[0])-1:
            # print(i, j)
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
            
        return False