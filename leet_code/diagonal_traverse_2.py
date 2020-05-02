class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            row = i-1
            ans.append(nums[i][0])
            for j in range(1, len(nums)):
                if row >= 0:
                    if j < len(nums[row]):
                        ans.append(nums[row][j])
                else:
                    break
        
                row -= 1
        max_col_len = 0
        
        for i in range(len(nums)):
            max_col_len = max(max_col_len, len(nums[i]))
        
        
        for i in range(1, max_col_len):
            
            if i < len(nums[-1]):
                ans.append(nums[len(nums)-1][i])
            
            row = len(nums) - 2
            col = i+1
            while row >= 0:
                if col < len(nums[row]):
                    ans.append(nums[row][col])
                row -= 1
                col += 1
            
        return ans


from collections import OrderedDict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
    
        d = OrderedDict()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if j+i in d.keys():
                    d[(j+i)].append(nums[i][j])
                else:
                    d[(j+i)] = [nums[i][j]]
        
        print(d)

        for i in d.keys():
            for num in range(len(d[i])-1, -1, -1):
                ans.append(d[i][num])
        return ans


[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
[[1,2,3],[4],[5,6,7],[8],[9,10,11]]
[[1,2,3,4,5,6]]
[[1,4,5,6], [4], [2, 4, 5,1], [7, 1]]