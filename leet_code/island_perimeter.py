# https://leetcode.com/problems/island-perimeter/
# Google, Hash Table

def islandPerimeter(grid: List[List[int]]) -> int:
    d = {0: 4, 1: 3, 2: 2, 3: 1, 4:0}
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                temp = 0
                row = i - 1
                column = j
                
                if row >= 0:
                    if grid[row][column] == 1:
                        temp += 1
                
                    
                row = i + 1
                column = j
                
                if row <= len(grid)-1:
                    if grid[row][column] == 1:
                        temp += 1
                

                
                row = i
                column = j - 1
            
                if column >= 0:
                    if grid[row][column] == 1:
                        temp += 1
                
                
                row = i
                column = j + 1
                
                if column <= len(grid[0])-1:
                    if grid[row][column] == 1:
                        temp += 1
                print(temp)
                ans += d[temp]
                
    return ans