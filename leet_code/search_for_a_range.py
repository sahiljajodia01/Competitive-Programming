# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/


######## An O(logn) solution using binary search. Using two binary search functions to find the left and right indexes #######
######## This could have been written in one function using conditional statement ########
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sol = [float('inf'), float('-inf')]
        
        def left_binary_search(nums, start, end, sol):
            
            if start <= end:
                mid = int(start + (end-start)/2)
                
                if nums[mid] == target:
                    # print("Mid: ", mid, "Value: ", nums[mid], "Left: ", sol[0])
                    if mid < sol[0]:
                        sol[0] = mid
                        # print(sol[0])
                    left_binary_search(nums, start, mid-1, sol)
                elif nums[mid] > target:
                    left_binary_search(nums, start, mid-1, sol)
                else:
                    left_binary_search(nums, mid+1, end, sol)

        
        def right_binary_search(nums, start, end, sol):
            
            
            if start <= end:
                mid = int(start + (end-start)/2)
                
                if nums[mid] == target:
                    if mid > sol[1]:
                        sol[1] = mid
                        # print(sol[1])
                    right_binary_search(nums, mid+1, end, sol)
                elif nums[mid] > target:
                    right_binary_search(nums, start, mid-1, sol)
                else:
                    right_binary_search(nums, mid+1, end, sol)
                    
        
        left_binary_search(nums, 0, len(nums)-1, sol)
        right_binary_search(nums, 0, len(nums)-1, sol)
        
        if sol[0] == float('inf') and sol[1] == float('-inf'):
            return [-1, -1]
        
        return sol