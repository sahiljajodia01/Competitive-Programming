# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

##### A standard DFS solution. If we do not want the input to modify we can use a visited array which ######
##### will however increase space required ######
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def safe(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0' or grid[row][col] == '-1':
                return False
            
            return True
        
        def dfs(grid, row, col):
            if not safe(grid, row, col):
                return
            
            grid[row][col] = '-1'
            
            dfs(grid, row+1, col)
            dfs(grid, row-1, col)
            dfs(grid, row, col+1)
            dfs(grid, row, col-1)
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '-1'
                    
                    dfs(grid, i+1, j)
                    dfs(grid, i-1, j)
                    dfs(grid, i, j+1)
                    dfs(grid, i, j-1)
                    ans += 1
                    
        return ans