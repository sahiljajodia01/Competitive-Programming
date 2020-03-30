# https://leetcode.com/problems/maximal-square/


###### This is a bottom up DP solution in O(mn) time. The intuition here is to check the check the left, top and top left element
##### in the matrix and accordingly store the square values in the matrix.
####### The brute force solution for this would take O((mn)^2) time.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_ = 0
        # dp = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 1 and int(matrix[i][j]) > max_:
                    # print("Inside 1st if")
                    max_ = int(matrix[i][j])
                
                if i-1 >= 0 and j-1 >= 0 and int(matrix[i][j]) > 0:
                    if int(matrix[i][j-1]) > 0 and int(matrix[i-1][j]) > 0 and int(matrix[i-1][j-1]) > 0:
                        # print("Inside 2nd if")
                        matrix[i][j] = str(min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1) # str(max(int(matrix[i-1][j-1])+1, int(matrix[i][j])))
                        
                        max_ = max(int(matrix[i][j]), max_)
        # print(matrix)                    
        return max_ ** 2