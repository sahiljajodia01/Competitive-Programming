# https://leetcode.com/problems/cheapest-flights-within-k-stops/


####### My solution using Djikstra's algorithm. Using Priority Queue internally for Djikstra's #######
####### Got it wrong initially 4 times ########
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        visited = [0] * n
        dist = [float('inf')] * n
        dist[src] = 0
        
        graph = {i:[] for i in range(n)}
        
        for i in range(len(flights)):
            u, v, d = flights[i]
            graph[u].append([v, d])

        pq = []
        
        heapq.heappush(pq, [dist[src], src, 0])
        
        while pq != []:
            value, index, stops = heapq.heappop(pq)
            visited[index] = 1

            ###### This ######
            if value < dist[index]:
                dist[index] = value
            
            if index == dst:
                continue

            #### or you can do #####
            # if index == dst:
            #     return value
            
            for i in range(len(graph[index])):
                node, d = graph[index][i]

                if visited[node] == 1:
                    continue
                
                if (stops) <= (K):
                    new_val = value + d
                    dist[node] = new_val
                    heapq.heappush(pq, [dist[node], node, stops+1])
        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]



####### Some of the test cases ########
3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
1
3
[[0,1,100],[1,2,100],[0,2,100]]
0
2
1
5
[[0,1,100], [0,3,300], [1,2,200], [2,3,100], [1,4,600], [2,4,200]]
0
4
1
5
[[0,1,100], [0,3,300], [1,2,200], [2,3,100], [1,4,600], [2,4,200]]
0
4
2
5
[[0,1,100], [0,3,300], [1,2,200], [2,3,100], [1,4,600], [2,4,200]]
0
3
2
5
[[0,1,100], [0,3,300], [1,2,200], [2,3,100], [1,4,600], [2,4,200]]
0
3
0
5
[[0,1,100], [0,3,300], [1,2,200], [2,3,100], [1,4,600], [2,4,200]]
0
3
1
5
[[0,1,100], [0,3,300], [1,2,200], [2,3,100], [1,4,600], [2,4,200]]
0
4
0
5
[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
2
1
1
4
[[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
0
3
1
5
[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
0
2
2
10
[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
6
0
7