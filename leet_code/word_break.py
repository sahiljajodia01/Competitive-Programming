# https://leetcode.com/problems/word-break/submissions/


########## Soluton using DP. ############
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {}
        
        for i in range(len(wordDict)):
            d[wordDict[i]] = 1
            
        q = [0]
        
        while q != []:
            ans = ""
            # print(q)
            first = q.pop(0)
            for j in range(first, len(s)):
                ans += s[j]
                # print(ans)
                if ans in d.keys():
                    if j == len(s) - 1:
                        return True
                    
                    if (j+1) not in q:
                        q.append(j+1)
            
        # print('-------------')
        return False