# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/

# My original solution that I attempted. It is correct but overly complicated
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        sorted_interval = sorted(intervals, key=lambda x: x[0])
        # print(sorted_interval)
        prev = sorted_interval[0]
        sol = []
        for i in range(1, len(sorted_interval)):
            # print(sorted_interval)
            if sorted_interval[i][0] == prev[0]:
                if sorted_interval[i][1] > prev[1]:
                    prev[0], prev[1] = 'a', 'a'
                    prev = sorted_interval[i]
                else:
                    sorted_interval[i][0], sorted_interval[i][1] = 'a', 'a'
            else:
                if sorted_interval[i][0] <= prev[1]:
                    if sorted_interval[i][1] <= prev[1]:
                        sorted_interval[i][0], sorted_interval[i][1] = 'a', 'a'
                    else:
                        prev[1] = sorted_interval[i][1]
                        sorted_interval[i][0], sorted_interval[i][1] = 'a', 'a'
                else:
                    prev = sorted_interval[i]
                        
        for i in range(len(sorted_interval)):
            if sorted_interval[i] != ['a', 'a']:
                sol.append(sorted_interval[i])
                
        return sol


# The much more simplified and clean solution from the discussion section
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        sorted_interval = sorted(intervals, key=lambda x: x[0])
        
        sol = []
        counter = 0
        for interval in sorted_interval:
            if sol == [] or sol[counter-1][1] < interval[0]:
                sol.append(interval)
                counter += 1
            else:
                sol[counter-1][1] = max(sol[counter-1][1], interval[1])
                
        return sol