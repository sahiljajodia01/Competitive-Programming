# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

###### Simple hashmap solution #######
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
                
        for key, value in d.items():
            if value > len(nums)//2:
                return key
            
        return nums[-1]