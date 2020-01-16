# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/


###### This is a two pass solution. Using counting sort to creating array of frequency of distinct elements. #######
###### Then replacing it in the original array #######
###### I did not understand the one pass algorithm which is given in discussion ######
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0]*3
        
        for i in range(len(nums)):
            a[nums[i]] += 1
        
        count = 0
        for i in range(len(a)):
            for j in range(a[i]):
                nums[count] = i
                count += 1