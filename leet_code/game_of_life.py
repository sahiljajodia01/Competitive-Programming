# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/831/


####### Inplace O(mn) time solution #######
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        neighbours = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                ones = 0
                for n in neighbours:
                    # row, col = ((i - n[0]) % len(board)), ((j - n[1]) % len(board[0]))
                    row, col = ((i - n[0])), ((j - n[1]))
                    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                        continue
                    if board[row][col] == 1 or board[row][col] == -1:
                        ones += 1
                
                if curr == 0:
                    if ones == 3:
                        board[i][j] = 2
                else:
                    if 2 <= ones <= 3:
                        continue
                    else:
                        board[i][j] = -1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0