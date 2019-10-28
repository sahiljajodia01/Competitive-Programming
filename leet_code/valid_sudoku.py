# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         num_count_dict = {
#             "1": 1,
#             "2": 1,
#             "3": 1,
#             "4": 1,
#             "5": 1,
#             "6": 1,
#             "7": 1,
#             "8": 1,
#             "9": 1
#         }
        
        
#         size = len(board)
#         for i in range(size):
#             num_copy = num_count_dict.copy()
            
#             for j in range(size):
#                 if board[i][j] in num_copy.keys():
#                     if num_copy[board[i][j]] != 0:
#                         num_copy[board[i][j]] -= 1
#                     else:
#                         return False
        
        
#         for i in range(size):
#             num_copy = num_count_dict.copy()

#             for j in range(size):
#                 if board[j][i] in num_copy.keys():
#                     if num_copy[board[j][i]] != 0:
#                         num_copy[board[j][i]] -= 1
#                     else:
#                         return False
                    
#         for i in range(0, size, 3):
#             for j in range(0, size, 3):
#                 num_copy = num_count_dict.copy()
                
#                 for k in range(i, i+3):
#                     for l in range(j, j+3):
#                         if board[k][l] in num_copy.keys():
#                             if num_copy[board[k][l]] != 0:
#                                 num_copy[board[k][l]] -= 1
#                             else:
#                                 return False
                            
#         return True