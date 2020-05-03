# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        for i in range(len(J)):
            if J[i] not in d.keys():
                d[J[i]] = 1
        
        ans = 0
        for i in range(len(S)):
            if S[i] in d.keys():
                ans += 1
        
        return ans