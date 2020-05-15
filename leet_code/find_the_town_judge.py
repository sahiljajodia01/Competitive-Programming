# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = {i:{} for i in range(1, N+1)}
        
        for i in range(len(trust)):
            x, y = trust[i]
            
            d[x][y] = 1
            
        # print(d)
        
        count = []
        for i in d.keys():
            if len(d[i]) == 0:
                count.append(i)
        
        if len(count) > 1 or len(count) == 0:
            return -1
        
        judge = count[0]
        
        for i in d.keys():
            if i != judge:
                if judge not in d[i].keys():
                    return -1
            else:
                if judge in d[i].keys():
                    return -1
        
        return judge