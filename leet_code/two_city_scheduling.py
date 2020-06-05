# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

##### Sorting the array based on difference of 1st ele and 2nd ele ######
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: (x[0]-x[1]))
        
        ans = 0
        # print(costs)
        n = len(costs)
        for i in range(n//2):
            ans += costs[i][0]
        
        for i in range(n//2, n):
            ans += costs[i][1]
        
        return ans