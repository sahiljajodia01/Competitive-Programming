# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

###### A very simple solution #########
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(0, numRows):
            temp = [0] * (i+1)
            for j in range(0, i+1):
                if j == 0 or j == len(temp) - 1:
                    temp[j] = 1
                else:
                    temp[j] = ans[i-1][j-1] + ans[i-1][j]
            
            ans.append(temp)
        
        return ans