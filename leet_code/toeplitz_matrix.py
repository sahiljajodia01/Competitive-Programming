# https://leetcode.com/problems/toeplitz-matrix/
# Google, Array


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    row = len(matrix)
    column = len(matrix[0])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0:
                continue
            else:
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
                
    return True