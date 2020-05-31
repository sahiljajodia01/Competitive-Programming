# https://leetcode.com/problems/as-far-from-land-as-possible/


###### My solution. Givs TLE. I am doing BFS on every zero and check how far it is from one and updating max_.
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        isOne = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    isOne = True
                    break
        
        if isOne == False:
            return -1
        
        max_ = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ele = grid[i][j]
                
                if ele == 1:
                    continue
                
                q = [[i, j]]
                count = 1
                while q:
                    temp = []
                    flag = False
                    for k in range(len(q)):
                        x, y = q[k]
                        
                        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                        
                        for n in neighbors:
                            x1, y1 = (x + n[0]), (y + n[1])
                            
                            if x1 >= 0 and x1 < len(grid) and y1 >= 0 and y1 < len(grid[0]):
                                if grid[x1][y1] == 1:
                                    max_ = max(max_, count)
                                    flag = True
                                    break
                                else:
                                    temp.append([x1, y1])
                        
                        if flag == True:
                            break
                    
                    if flag == True:
                        break
                    
                    q = temp
                    count += 1
            
        return max_



########## Solution I saw from discussion. It does BFS in only one iteration. Very clever idea of not doing BFS on every 0.
########## Rather starting from all ones and checking if the neighbours are zero.
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ones = 0
        zeroes = 0
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i, j])
                    ones += 1
                else:
                    zeroes += 1
        
        if ones == len(grid)*len(grid[0]) or zeroes == len(grid)*len(grid[0]):
            return -1
        
        count = -1
        while q:
            temp = []
            
            for i in range(len(q)):
                x, y = q[i]
                
                neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                
                for n in neighbors:
                    x1, y1 = (x + n[0]), (y + n[1])
                    
                    if x1 >= 0 and x1 < len(grid) and y1 >= 0 and y1 < len(grid[0]) and grid[x1][y1] == 0:
                        grid[x1][y1] = 1
                        temp.append([x1, y1])
            
            q = temp
            count += 1
        
        return count