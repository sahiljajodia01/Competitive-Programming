# https://leetcode.com/contest/biweekly-contest-25/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        sol = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                sol.append(True)
            else:
                sol.append(False)
                
        return sol