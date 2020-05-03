# https://leetcode.com/problems/rotting-oranges/

####### Straightforward BFS solution ##########
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
        
        minute = 0
        while q != []:
            # print(q)
            minute += 1
            temp = []
            for i in range(len(q)):
                x, y = q[i]
                
                neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                
                for n in neighbours:
                    xn, yn = (x + n[0]), (y+ n[1])
                    
                    if xn < 0 or xn >= len(grid) or yn < 0 or yn >= len(grid[0]) or grid[xn][yn] == 0 or grid[xn][yn] == 2:
                        continue
                    
                    grid[xn][yn] = 2
                    
                    
                    if [xn, yn] not in temp:
                        temp.append([xn, yn])
            
            q = temp
        
        # print(minute)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        if minute == 0:
            return 0
        
        return minute - 1