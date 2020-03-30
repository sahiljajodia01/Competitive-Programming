# https://leetcode.com/problems/unique-paths-ii/

########## Top down DP solution. Just barely accepted (beats only 5%) ###########
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        arr = []
        for i in range(len(obstacleGrid)):
            temp = []
            for j in range(len(obstacleGrid[0])):
                temp.append(-1)
            arr.append(temp)
            
        def solve(m, n, arr, grid):
            # print(n, m)
            # print(arr)
            if m < 0 or n < 0:
                return 0
            elif arr[n][m] > 0:
                return arr[n][m]
            elif m == 0 and n == 0:
                if grid[n][m] == 0:
                    return 1
                else:
                    return 0
            elif grid[n][m] == 1:
                return 0
            else:
                arr[n][m] = solve(m-1, n, arr, grid) + solve(m, n-1, arr, grid)
                return arr[n][m]
        
        return solve(len(obstacleGrid[0])-1, len(obstacleGrid)-1, arr, obstacleGrid)


########## Bottom UP O(1) DP solution. Also short and clean code ###########
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] * 1
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] * 1
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                    
        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]