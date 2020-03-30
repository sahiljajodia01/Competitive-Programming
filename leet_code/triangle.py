# https://leetcode.com/problems/triangle/


####### Dynamic programming solution using a 2d dp table. ########
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        arr = []

        for i in range(len(triangle)):
            temp = []
            
            for j in range(len(triangle[i])):
                temp.append(-1)
                
            arr.append(temp)
        arr[0][0] = triangle[0][0] 
        
        for i in range(1, len(triangle)):
            
            arr[i][0] = arr[i-1][0] + triangle[i][0]
            for j in range(1, len(triangle[i])-1):
                prev_left = arr[i-1][j-1]
                prev_right = arr[i-1][j]
                
                arr[i][j] = triangle[i][j] + min(prev_left, prev_right)
                
            arr[i][-1] = arr[i-1][-1] + triangle[i][-1]
            
        # print(arr)
        return min(arr[-1])