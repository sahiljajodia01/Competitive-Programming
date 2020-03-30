# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

############### A very naive approach ##################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        ans = ""
        counter = 0
        flag = 0
        while counter < len(strs[0]):
            initial = strs[0][counter]
            for i in range(1, len(strs)):
                if len(strs[i]) > counter:
                    if strs[i][counter] == initial:
                        continue
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
                    
            if flag == 1:
                break
            else:
                ans += initial
                
            counter += 1
            flag = 0
            
        return ans



######## Similar complexity to previous but slightly different solution #########
from collections import defaultdict
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        
        smallest_length = float('inf')
        for i in range(len(strs)):
            if len(strs[i]) < smallest_length:
                smallest_length = len(strs[i])
        
        if smallest_length == float('inf'):
            smallest_length = 0
        
        for i in range(smallest_length):
            char = strs[0][i]
            flag = False
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    flag = True
                    break
            
            if flag == True:
                break
            else:
                ans.append(char)
        
        return "".join(ans)


######## Another solution can be to find the smallest and the longest string and then checking for the common prefix between
######## the two #########