# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

################ Kadane's Algorithm ###############
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        temp = 0
        for i in range(len(nums)):
            print(temp, max_sum)
            if temp < 0:
                temp = 0
                
            temp += nums[i]
            if temp > max_sum:
                max_sum = temp
            
        return max_sum