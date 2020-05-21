[1,2,0]
[1,1]
[10,4,16,54,17,-7,21,15,25,31,61,1,6,12,21,46,16,56,54,12,23,20,38,63,2,27,35,11,13,47,13,11,61,39,0,14,42,8,16,54,50,12,-10,43,11,-1,24,38,-10,13,60,0,44,11,50,33,48,20,31,-4,2,54,-6,51,6]
[1,0]
[1,3,3]
[3,4,-1,1]
[7,8,9,11,12]
[1]
[-10]
[2]
[1, 1000]
[]

# https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/832/


####### I had to look at the discussion for this solution. However a question with very similar concept shows how
####### to solve this - https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/ 
####### There is also another solution using swapping in the discussion #######
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        length = len(nums)
        for i in range(len(nums)):        
            if nums[i] < 0 or nums[i] >= length:
                nums[i] = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nums[i] % length] += length
        
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] // length == 0:
                return i
        
        return length