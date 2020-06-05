# https://leetcode.com/problems/burst-balloons/


###### A very hard DP problem. I had to look at the solution in the discussion #######
from collections import deque


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = deque(nums)
        
        nums.appendleft(1)
        nums.append(1)
        
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        # print(nums)
        for i in range(1, len(nums)-1):
            for j in range(1, len(nums)-i):
                start = j
                end = start + i - 1
                
                max_ = 0
                
                for k in range(start, end+1):
                    temp = dp[start][k-1] + dp[k+1][end] + (nums[start-1]*nums[k]*nums[end+1])
                    max_ = max(max_, temp)
                    
                dp[start][end] = max_
        # print(dp)
        return dp[1][len(nums)-2]