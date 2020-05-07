# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


###### The problem description was not clear on how to arrange the values for a particular vertical order ######
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.d = defaultdict(list)
        
        if root:
            q = [[root, 0]]
        else:
            q = []
            
        while q:
            temp = []
            d = defaultdict(list)
            for i in range(len(q)):
                ele, depth = q[i]
                
                d[depth].append(ele.val)
                
                if ele.left:
                    temp.append([ele.left, depth-1])
                
                if ele.right:
                    temp.append([ele.right, depth + 1])
            
            for i in d.keys():
                self.d[i].extend(sorted(d[i]))
            q = temp
            
        sorted_d = {k:v for k,v in sorted(self.d.items())}
        
        return sorted_d.values()