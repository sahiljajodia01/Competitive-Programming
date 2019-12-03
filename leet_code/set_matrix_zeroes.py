# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

######### Using space for storing the indexes of elements which are zero #########
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes_arr = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroes_arr.append((i, j))
        
        for i, j in zeroes_arr:
            for k in range(len(matrix[i])):
                matrix[i][k] = 0
            for k in range(len(matrix)):
                matrix[k][j] = 0


######### Inplace solution ##########
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes_arr = []
        first_column = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if j == 0:
                        first_column = True
                        matrix[i][0] = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if first_column == True:
            for i in range(len(matrix)):
                matrix[i][0] = 0