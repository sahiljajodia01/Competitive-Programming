# https://leetcode.com/problems/critical-connections-in-a-network/submissions/


######## Naive solution using BFS. TLE for O(n^2) ##############
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            graph.append(temp)

        ans = []
        
        for i in range(len(connections)):
            for j in range(len(connections)):
                x, y = connections[j]

                graph[x][y], graph[y][x] = 1, 1
        
        for i in range(len(connections)):
            # print(connections[i])
            # print(graph)
            visited = []
            q = [0]
            
            while q != []:
                # print(q, visited)
                ele = q.pop(0)
                visited.append(ele)
                for j in range(len(graph[0])):
                    if ele == connections[i][0] and j == connections[i][1]:
                        continue
                    if ele == connections[i][1] and j == connections[i][0]:
                        continue
                        
                    if j not in q and j not in visited and graph[ele][j] == 1:
                        q.append(j)
            
            
            # print(visited)
            if len(visited) < n:
                # print("ans")
                ans.append(connections[i])
            # print('--------------')
        return ans



########### O(n) accepted solution using articulation bridges algorithm ###########
####### Referred this video - https://www.youtube.com/watch?v=aZXi1unBdJA #########
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.count = 0
        self.bridges = []
        
        d = {i:[] for i in range(n)}
        for i in range(len(connections)):
            x, y = connections[i]
            
            d[x].append(y)
            d[y].append(x)

    
        ids = [-1] * n
        low_link = [-1] * n
        visited = [0] * n
        
        # print(d)
        def dfs(node, parent):
            # print(node, parent)
            ids[node] = self.count
            low_link[node] = self.count
            visited[node] = 1
            self.count += 1
            
            for to in d[node]:
                if to == parent:
                    continue
                elif visited[to] == 0:
                    dfs(to, node)
                
                    low_link[node] = min(low_link[node], low_link[to])
                    if ids[node] < low_link[to]:
                        self.bridges.append([node, to])
                else:
                    low_link[node] = min(low_link[node], ids[to])
        
        
        for i in d.keys():
            if visited[i] == 0:
                dfs(i, -1)
        # print(ids)
        # print(low_link)
        return self.bridges