# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/


####### A dumb recursive O(n) solution. #######
####### Here I am declaring final_index in a way of list because list is an mutable data type so we can change it #######
####### via reference inside the recursive function #######
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        final_index = [0]
        def solve(nums, final_index, start, end):
            if start > end:
                return
            mid = int(start + (end - start)/2)
            if len(nums) == 1:
                return
            if mid == 0:
                prev = float('-inf')
                curr = nums[mid]
                nex = nums[mid+1]
            elif mid == len(nums) - 1:
                prev = nums[mid-1]
                curr = nums[mid]
                nex = float('-inf')
            else:
                prev = nums[mid-1]
                curr = nums[mid]
                nex = nums[mid+1]
                
            if curr > prev and curr > nex:
                print(mid)
                final_index[0] = mid
            else:
                solve(nums, final_index, start, mid-1)
                solve(nums, final_index, mid+1, end)
            
        solve(nums, final_index, 0, len(nums)-1)
        return final_index[0]


######## A recursive binary search O(logn) solution. Got this from the solutions provided ########
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def solve(nums, start, end):
            if start == end:
                return end
            
            mid = int(start + (end - start)/2)
            
            if nums[mid] > nums[mid+1]:
                return solve(nums, start, mid)
            else:
                return solve(nums, mid+1, end)
            
        return solve(nums, 0, len(nums)-1)