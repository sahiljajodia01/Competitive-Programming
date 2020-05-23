# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/

###### Two pointer approach ######
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        count = 0
        sol = []
        for i in range(len(A)):
            a = A[i][0]
            b = A[i][1]
            
            count = max(0, count-1)
            while count < len(B) and B[count][0] <= b:
                c = B[count][0]
                d = B[count][1]
                
                if d >= a:
                    sol.append([max(a, c), min(b, d)])
                count += 1
        return sol