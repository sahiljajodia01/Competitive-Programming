# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary_search(beg, end, version):
            if beg <= end:
                # mid = (beg+end)//2       Should not use this. This can cause overflow.
                mid = beg + (end-beg)//2
                if isBadVersion(mid):
                    if mid < version:
                        version = mid
                    version = binary_search(beg, mid-1, version)
                else:
                    version = binary_search(mid+1, end, version)
                    
            return version
        min_bad_version = binary_search(1, n, n)            
        return min_bad_version