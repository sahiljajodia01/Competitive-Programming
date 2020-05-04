# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

######## Solve by very naive method. This is to be solved by bit manipulation. #######
######## There are bit manipulation solutions in the discussions #######
class Solution:
    def findComplement(self, num: int) -> int:
        l = list(str(bin(num)))
        
        for i in range(len(l)-1, 1, -1):
            if l[i] == '0':
                l[i] = '1'
            else:
                l[i] = '0'
                
        return int(''.join(l), 2)