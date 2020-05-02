# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
###### This problem is very very similar to - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/ ######



####### My solution. Works pretty well ########
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(l, matrix[i][j])
        
        return heapq.nsmallest(k, l)[-1]



######### A better solution that I saw in discusion ##########
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        queue = []
        
        if len(matrix) > 0 and len(matrix[0]) > 0:
            heapq.heappush(queue, [matrix[0][0], 0, 0])
        
        sums = []
        
        while queue != [] and len(sums) < k:
            s, i, j = heapq.heappop(queue)
            sums.append(matrix[i][j])
            
            if i < len(matrix) and (j+1) < len(matrix[0]):
                heapq.heappush(queue, [matrix[i][j+1], i, j+1])
            
            if j == 0 and (i+1) < len(matrix) and j < len(matrix[0]):
                heapq.heappush(queue, [matrix[i+1][j], i+1, j])
        
        return sums[-1]