# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        
        while j < n:
            print(nums1, i, j)
            if nums1[i] <= nums2[j] and i < m:
                i += 1
                continue;
            else:
                if i < m:
                    for k in range(m, i, -1):
                        nums1[k] = nums1[k-1]
                    
                nums1[i] = nums2[j]
                i += 1
                j += 1
                m += 1