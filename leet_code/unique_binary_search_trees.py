# https://leetcode.com/problems/unique-binary-search-trees/


# Using a dp array to calculate the number of binary search trees
class Solution:
    def numTrees(self, n: int) -> int:
        d = [-1] * (n+1)
        d[0] = 1
        d[1] = 1
        
        
        for i in range(2, n+1):
            left = (i//2)
            left_ans = 0
            mid_ans = 0
            counter = 0
            for j in range(i-1, i-left-1, -1):
                left_ans += d[j] * d[counter]
                counter += 1
                
            if i % 2 != 0:
                mid_ans = d[left] * d[left]
            
            # print("left_ans = ", left_ans, ", mid_ans = ", mid_ans)
            d[i] = mid_ans + 2 * left_ans
                
        # print("------------------")
        return d[-1]