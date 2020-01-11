# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            level = [root]
        else:
            level = []
            
        while level != []:
            queue = []
            
            for i in range(len(level)):
                if i == len(level) - 1:
                    level[i].next = None
                else:
                    level[i].next = level[i+1]
                
                
                if level[i].left:
                    queue.append(level[i].left)
                
                if level[i].right:
                    queue.append(level[i].right)
        
            level = queue
            
        return root