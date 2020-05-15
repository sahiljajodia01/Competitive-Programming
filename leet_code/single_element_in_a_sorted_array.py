# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        def binary_search(nums):
            if len(nums) == 0:
                return -1
            elif len(nums) == 1:
                return nums[0]

            left, right = 0, len(nums) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                
                if nums[mid] == nums[mid-1] and nums[mid] < nums[mid+1]:
                    if mid % 2 != 0:
                        left = mid
                    else:
                        right = mid
                elif nums[mid] == nums[mid+1] and nums[mid] > nums[mid-1]:
                    if mid % 2 != 0:
                        right = mid
                    else:
                        left = mid
                elif nums[mid-1] < nums[mid] < nums[mid+1]:
                    return nums[mid]
            
            if right == len(nums)-1:
                return nums[right]
            
            if left == 0:
                return nums[left]
                
        return binary_search(nums)