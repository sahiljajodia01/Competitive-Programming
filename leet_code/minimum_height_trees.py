# https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = {}
        
        graph = {}
        for i in range(len(edges)):
            x, y = edges[i]
            
            if x in graph.keys():
                graph[x][y] = 1
            else:
                graph[x] = {y:1}
            
            if y in graph.keys():
                graph[y][x] = 1
            else:
                graph[y] = {x:1}
            
            if x in d.keys():
                d[x] += 1
            else:
                d[x] = 1
            
            if y in d.keys():
                d[y] += 1
            else:
                d[y] = 1
        
        # print(graph)   
        if len(d) == 0:
            d[0] = 0
        
        q = []
        
        for i in d.keys():
            if d[i] == 1:
                q.append(i)
                
                
        while n > 2:
            # print(q)
            temp = []
            
            for i in range(len(q)):
                n -= 1
                
                del d[q[i]]
                for i in graph[q[i]]:
                    if i in d.keys():
                        d[i] -= 1

                        if d[i] == 1:
                            temp.append(i)
            q = temp
        
        # print(d)
        return list(d)