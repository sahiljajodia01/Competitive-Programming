# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        if len(nums) > 0:
            nums[counter] = nums[0]
            counter += 1
        for i in range(1, len(nums)):
            if nums[i] == nums[counter-1]:
                continue
            else:
                nums[counter] = nums[i]
                counter += 1
        
        return counter