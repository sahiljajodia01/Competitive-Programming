# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/

######## Using DP. Very similar to Maximal Square problem on leetcode #######
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                left, up, diag = matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]
                
                if matrix[i][j] != 0 and left != 0 and up != 0 and diag != 0:
                    matrix[i][j] = min(left, up, diag) + 1
        
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count += matrix[i][j]
                
        return count


##### Even more shorter and classy solution from the discussions ######
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                left, up, diag = matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]
                
                matrix[i][j] *= min(left, up, diag) + 1
        
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count += matrix[i][j]
                
        return count