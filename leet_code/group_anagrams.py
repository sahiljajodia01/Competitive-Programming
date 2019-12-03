# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/


######## This was the solution that I saw on leetcode ###########
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        sol_set = []
        i = 0
        while i < len(strs):
            if tuple(sorted(strs[i])) not in d.keys():
                d[tuple(sorted(strs[i]))] = [strs[i]]
            else:
                d[tuple(sorted(strs[i]))].append(strs[i])
            
            i += 1
                
        return d.values()


####### This was my solution. This passed all but one test case ########
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        sol_set = []
        i = 0
        while i < len(strs):
            if strs[i] not in d.keys():
                temp = []
                temp.append(strs[i])
                d[strs[i]] = 1
                for j in range(i+1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        temp.append(strs[j])
                        d[strs[j]] = 1
                sol_set.append(temp)
            i += 1
        
        return sol_set