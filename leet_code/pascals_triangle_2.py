# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/


############ Recursive solution using only O(k) extra space as asked in question ##########
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def solve(row, ans, k, i):
            # print(ans)
            if k <= (i-1):
                ele = row[k] + row[k-1]
                ans.append(ele)
                return solve(row, ans, k+1, i) 
            else:
                return ans
        
        
        row = [1]
        
        if rowIndex == 0:
            return [1]
        
        for i in range(1, rowIndex+1):
            row = [1] + solve(row, [], 1, i) + [1]
        
        return row