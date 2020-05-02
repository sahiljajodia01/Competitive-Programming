# https://leetcode.com/problems/evaluate-division/


######### Using a graph based BFS approach to solve this problem. There is also a union-find based approach which i'll have to look at ########
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        reverse_d = {}
        counter = 0
        for i in range(len(equations)):
            for j in range(len(equations[i])):
                if equations[i][j] not in d.keys():
                    d[equations[i][j]] = counter
                    reverse_d[counter] = equations[i][j]
                    counter += 1
        
        graph = []
        
        for i in range(len(d)):
            temp = []
            
            for j in range(len(d)):
                temp.append(-1)
            
            graph.append(temp)
            
        for i in d:
            graph[d[i]][d[i]] = 1
        
        for i in range(len(equations)):
            graph[d[equations[i][0]]][d[equations[i][1]]] = values[i]
            graph[d[equations[i][1]]][d[equations[i][0]]] = 1/values[i]
        
        # print(graph)
        ans = []
        for query in queries:
            if query[0] not in d.keys() or query[1] not in d.keys():
                ans.append(-1)
                continue
            elif graph[d[query[0]]][d[query[1]]] != -1:
                ans.append(graph[d[query[0]]][d[query[1]]])
                continue
            # print("Query: ", query)
            q = [query[0]]
            final = 1
            total = [1]
            flag = False
            visited = []
            while q != []:
                # print(q, total, visited)
                temp = []
                temp_total = []
                for i in range(len(q)):
                    element = q[i]
                    visited.append(element)
                    ele = d[element]
                    curr_total = total[i]
                    for i in range(len(graph[0])):
                        if reverse_d[i] not in visited and graph[d[element]][i] != -1:
                            if reverse_d[i] == query[1]:
                                final = curr_total * graph[d[element]][i]
                                flag = True
                                break
                            temp.append(reverse_d[i])
                            temp_total.append((curr_total*graph[d[element]][i]))
                
                    if flag == True:
                        break
                if flag == True:
                    break
                
                q = temp
                total = temp_total
            if flag == False:
                ans.append(-1)
            else:
                ans.append(final)
            # print("--------------------")
        
        return ans