# https://leetcode.com/problems/clone-graph/


######## My solution ########
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node:
            q = [node]
        else:
            q = []
        
        arr = [None] * 101
        
        while q:
            # print(q)
            temp = []
            for i in range(len(q)):
                # print(q[i].val)
                if arr[q[i].val] == None:
                    arr[q[i].val] = Node(q[i].val)
                
                for j in range(len(q[i].neighbors)):
                    if arr[q[i].neighbors[j].val] == None:
                        # print(q[i].neighbors[j].val)
                        if q[i].neighbors[j] not in temp:
                            temp.append(q[i].neighbors[j])
                # print('------------')
            q = temp
        # print(arr)
        
        
        if node:
            q = [node]
        else:
            q = []
        
        visited = []
        while q:
            temp = []
            for i in range(len(q)):
                # print(q[i].val)
                visited.append(q[i].val)
                
                for j in range(len(q[i].neighbors)):
                    # print(q[i].neighbors[j].val)
                    if q[i].neighbors[j].val not in visited:
                        if q[i].neighbors[j] not in temp:
                            temp.append(q[i].neighbors[j])
                    
                    arr[q[i].val].neighbors.append(arr[q[i].neighbors[j].val])
                # print('----------------')
            q = temp
        if node == None:
            return None
        return arr[node.val]



####### Efficent and consice solution from the discussion #######
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q = deque()
        d = {}
        if node:
            q.append(node)
            initial_node = Node(node.val)
            d[node] = initial_node
        else:
            initial_node = None
            q = []
        
        while q:
            node = q.popleft()
            for j in range(len(node.neighbors)):
                if node.neighbors[j] not in d.keys():
                    new_node = Node(node.neighbors[j].val)
                    d[node.neighbors[j]] = new_node
                    d[node].neighbors.append(new_node)
                    q.append(node.neighbors[j])
                else:
                    d[node].neighbors.append(d[node.neighbors[j]])
        
        return initial_node


[[2,4],[1,3],[2,4],[1,3]]
[[]]
[]
[[2],[1]]
[[2, 3], [1, 4], [1, 4, 5], [2, 3, 6], [3, 7], [4, 7, 8], [5, 6], [6]]