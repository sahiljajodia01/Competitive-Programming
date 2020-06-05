###### https://leetcode.com/problems/is-graph-bipartite/


###### DFS solution for coloring graph problem. This problem is exactly similar to possible bipartition #######
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj_list = {i:{} for i in range(len(graph))}
        
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adj_list[i][graph[i][j]] = 1
        
        
        visited = [-1 for i in range(len(graph))]
        # print(adj_list)
        def dfs(adj_list, visited, node, color):
            
            if visited[node] != -1 and visited[node] != color:
                return False
            
            visited[node] = color
            # print(node, visited)
            ans = True
            for n in adj_list[node].keys():
                # print(n)
                if visited[n] == -1:
                    # print("Inside if")
                    ans &= dfs(adj_list, visited, n, 1-color)
                elif visited[n] != 1 - color:
                    # print("Inside else")
                    return False
                
                if ans == False:
                    return False
            
            return True
            
            
        
        for i in range(len(graph)):
            if visited[i] == -1:
                # visited[i] = 1 - visited[i]
                ans = dfs(adj_list, visited, i, 1)
                
                if not ans:
                    return False
        
        return True