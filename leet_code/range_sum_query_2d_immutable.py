# https://leetcode.com/problems/range-sum-query-2d-immutable/


######## Same trick as Range sum query 1d.
######## Summing all the rows one by one
######## In sum region method, just getting the total sum from row1 to row2. Effectively bringing the time
######## complexity fro O(n^2) to O(n)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        for i in range(len(matrix)):
            prev = 0
            for j in range(len(matrix[i])):
                matrix[i][j] += prev
                prev = matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            if col1 != 0:
                total += self.matrix[i][col2] - self.matrix[i][col1-1]
            else:
                total += self.matrix[i][col2]
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



######## Even better solution. Sum range method executed in O(1). Saw this in discussion forum.
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if len(matrix) != 0:
            for i in range(1, len(matrix[0])):
                self.matrix[0][i] += self.matrix[0][i-1]
        
        for i in range(1, len(matrix)):
            self.matrix[i][0] += self.matrix[i-1][0]
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                self.matrix[i][j] += self.matrix[i][j-1] + self.matrix[i-1][j] - self.matrix[i-1][j-1]
        
        # print(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        total = 0
        if row1 == 0 and col1 == 0:
            return matrix[row2][col2]
        elif row1 == 0:
            return matrix[row2][col2] - matrix[row2][col1-1]
        elif col1 == 0:
            return matrix[row2][col2] - matrix[row1-1][col2]
        else:
            return matrix[row2][col2] - matrix[row1-1][col2] - matrix[row2][col1-1] + matrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)