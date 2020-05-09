# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

###### Simple binary search template 1 solution ######
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def solve(num, beg, end):
            while beg <= end:
                mid = (beg + end)//2
                # print(beg, mid, end)
                if (mid * mid) == num:
                    return True
                elif (mid * mid) > num:
                    end = mid-1
                else:
                    beg = mid+1
            
            return False
        
        return solve(num, 0, num)