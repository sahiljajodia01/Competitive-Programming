# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first_ele = nums[0]
        second_ele = -1
        flag = 0
        counter = 1
        for i in range(1, len(nums)):
            counter += 1
            if first_ele > nums[i]:
                first_ele = nums[i]
            else:
                second_ele = nums[i]
                flag = 1
                break
        
        if flag == 0:
            return False
        
        for i in range(counter, len(nums)):
            print(nums[i], first_ele, second_ele)
            if second_ele < nums[i]:
                return True
            elif first_ele < nums[i]:
                second_ele = nums[i]
            else:
                first_ele = nums[i]
        
        return False