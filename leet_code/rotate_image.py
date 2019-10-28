# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         size = len(matrix)
#         for i in range(size):
#             for j in range(i, size):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
#         for i in range(size):
#             matrix[i] = matrix[i][::-1]