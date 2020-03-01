# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def solve(nums, start, end):
            if start == end:
                return end
            
            mid = int(start + (end - start)/2)
            
            if nums[mid] > nums[end]:
                return solve(nums, mid+1, end)
            else:
                return solve(nums, start, mid)
        
        def binary_search(nums, start, end, target):
            if start <= end:
                mid = int(start + (end - start)/2)
                # print("mid: ", mid, "start: ", start, "end: ", end)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(nums, mid+1, end, target)
                else:
                    return binary_search(nums, start, mid-1, target)
        
        if len(nums) == 0:
            return -1
        
        pivot = solve(nums, 0, len(nums)-1)
        print(pivot)
        left = nums[:(pivot)]
        right = nums[(pivot):]
        print(left, right)
        ans1 = binary_search(left, 0, len(left)-1, target)
        ans2 = binary_search(right, 0, len(right)-1, target)
        print(ans1, ans2)
        
        if ans1 != None:
            return ans1
        elif ans2 != None:
            return (len(left) + ans2)
        else:
            return -1