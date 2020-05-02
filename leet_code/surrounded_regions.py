class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         parents = []
        
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 if board[i][j] == 'X':
#                     parents.append(1)
#                 else:
#                     parents.append(0)
        
        
        
        
#         def find(x):
#             root = x
            
#             while root != parents[root]:
#                 root = parents[root]
            
#             while parents[x] != root:
#                 n = parents[x]
#                 parents[x] = root
#                 x = n
            
#             return root
        
#         def union(x, y):
#             par1 = find(x)
#             par2 = find(y)
            
#             if par1 == par2:
#                 return
            
#             parents[par1] = par2
            
        
#         neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         for i in range(1, len(board)-1):
#             for j in range(1, len(board[i])-1):
#                 flag = False
#                 for k in range(len(neighbours)):
#                     x = i + neighbours[k][0]
#                     y = j + neighbours[k][1]
                    
#                     if board[x][y] == 'O' and (x == 0 or x == len(board)-1 or y == 0 or y == len(board[0]) - 1):
#                         flag = True
#                         break
                
#                 if flag == True:
#                     continue
                
#                 for k in range(len(neighbours)):
#                     x = i + neighbours[k][0]
#                     y = j + neighbours[k][1]
                    
#                     if board[i][j] == 'O' and board[x][y] == 'X':
#                         board[i][j] = 'X'

#         def safe(grid, row, col):
#             if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0' or grid[row][col] == '-1':
#                 return False
            
#             return True
        
#         def dfs(grid, row, col):
#             if not safe(grid, row, col):
#                 return
            
#             grid[row][col] = '-1'
            
#             dfs(grid, row+1, col)
#             dfs(grid, row-1, col)
#             dfs(grid, row, col+1)
#             dfs(grid, row, col-1)
            
#         ans = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     grid[i][j] = '-1'
                    
#                     dfs(grid, i+1, j)
#                     dfs(grid, i-1, j)
#                     dfs(grid, i, j+1)
#                     dfs(grid, i, j-1)
#                     ans += 1
                    
#         return ans
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and board[i][j] == 'O':
                    ele = board[i][j]

                    q = [(i, j)]

                    while q != []:
                        row, col = q.pop(0)

                        if (row >= 0 and row < len(board)) and (col >= 0 and col < len(board[0])):
                            if board[row][col] == 'O':
                                board[row][col] = 'Y'

                                neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]

                                for neighbour in neighbours:
                                    q.append((row-neighbour[0], col-neighbour[1]))
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'
        
        return board





[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
[["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]
[["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","X"]]
[["X","X","X","X","X"],["X","X","O","O","X"],["X","O","X","X","X"],["X","X","O","O","O"],["X","X","O","X","X"]]
[["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]