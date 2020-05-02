# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
###### This problem is very very similar to - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/ ######


####### My solution. Very bad solution but still accepted. Only beats 5% ########
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []
        sum_arr = []
        index = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pairs.append([nums1[i], nums2[j]])
                sum_arr.append((nums1[i] + nums2[j]))
        
        
        heap_arr = sum_arr.copy()
        
        heapq.heapify(heap_arr)
        
        smallest = heapq.nsmallest(k, heap_arr)
        
        ans = []
        for i in range(len(smallest)):
            for j in range(len(sum_arr)):
                if sum_arr[j] == smallest[i] and j not in index:
                    ans.append(pairs[j])
                    index.append(j)
                    break
        
        return ans



######### A good intuitive solution I saw on discussions #########
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:     
        pairs = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pairs.append([nums1[i], nums2[j]])
        
        return heapq.nsmallest(k, pairs, key=sum)



####### A not so intuitve but very fast solution seen in discussion forum. ########
####### To understand this - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions #######
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        
        if len(nums1) > 0 and len(nums2) > 0:
            heapq.heappush(queue, [nums1[0]+nums2[0], 0, 0])
        
        pairs = []
        
        while queue != [] and len(pairs) < k:
            s, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            
            if i < len(nums1) and (j+1) < len(nums2):
                heapq.heappush(queue, [nums1[i]+nums2[j+1], i, j+1])
            
            if j == 0 and (i+1) < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i+1]+nums2[j], i+1, j])
        
        return pairs