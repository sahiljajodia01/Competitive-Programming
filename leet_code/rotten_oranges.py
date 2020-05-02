# https://leetcode.com/problems/rotting-oranges/

####### Straightforward BFS solution ##########
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])
                    
                    
        for i in range(len(q)):
            grid[q[i][0]][q[i][1]] = 1
        
        minute = -1
        while q != []:
            # print(q)
            minute += 1
            temp = []
            for i in range(len(q)):
                x, y = q[i]
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0 or grid[x][y] == 2:
                    continue
                grid[x][y] = 2
                
                neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                
                for n in neighbours:
                    if [x - n[0], y - n[1]] not in temp:
                        temp.append([x - n[0], y - n[1]])
            
            q = temp
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        if minute == -1:
            return 0
        
        return minute - 1