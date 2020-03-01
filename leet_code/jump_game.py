# https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/

# O(n^2) dynamic porgramming solution. 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        
        def solve(nums, index, dp):
            # print(index, dp)
            if index == len(nums) - 1:
                return True
            
            for i in range(1, nums[index]+1):
                # print("index: ", index, "i: ", i)
                if dp[index+i] == 1:
                    return True
                elif dp[index+i] == 0:
                    continue
                else:
                    if solve(nums, index+i, dp):
                        dp[index+i] = 1
                        return True
                    else:
                        dp[index+i] = 0
                        continue
    
            return False
        return solve(nums, 0, dp)


# O(n) solution but a little non intuitive to think.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good = len(nums) - 1
    
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= last_good:
                last_good = i
                
        if last_good == 0:
            return True
        else:
            return False