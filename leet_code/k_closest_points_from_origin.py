# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/


##### My heap solution. But still gives O(nlogn) complexity in worst case. There is a better approach using
##### divide and conquer from the solutions ########
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        ######### Standard heap solution. Complexity - O(nlogn) ########
        pq = []
        
        for i in range(len(points)):
            heapq.heappush(pq, [(points[i][0]**2 + points[i][1]**2), points[i]])
            
        ans = []
        while K:
            dist, coord = heapq.heappop(pq)
            ans.append(coord)
            K -= 1
            
        return ans
    
    
        
        ######### Heapify solution. Slightly better. Complexity - O(nlog(k)) ########
        pq = []
        
        for i in range(len(points)):
            pq.append([(points[i][0]**2 + points[i][1]**2), points[i]])
            
        heapq.heapify(pq)
        ans = []
        while K:
            dist, coord = heapq.heappop(pq)
            ans.append(coord)
            K -= 1
            
        return ans