# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/


######## There are other solutions as well on the link above apart from the naive sorting one ########
####### Using sum formula and then subtracting the actual sum from the total sum to get the answer #######
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = (len(nums)*(len(nums) + 1))//2
        
        actual_sum = 0
        
        for i in range(len(nums)):
            actual_sum += nums[i]
         
        return total_sum - actual_sum


####### Using hashmap ########
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = 1
                
        for i in range(len(nums)+1):
            if i not in d.keys():
                return i