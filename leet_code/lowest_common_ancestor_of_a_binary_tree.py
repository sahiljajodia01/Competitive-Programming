# https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/


###### Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_path = []
        self.q_path = []
        
        def solve(root, p, q, path):
            if root.val == p.val:
                self.p_path = path
            
            if root.val == q.val:
                self.q_path = path
                
            if root.left:
                solve(root.left, p, q, path + [root.left])
            
            if root.right:
                solve(root.right, p, q, path + [root.right])
        
        if root == None:
            return None
        
        ans = None
        solve(root, p, q, [root])
        for i in range(min(len(self.p_path), len(self.q_path))):
            if self.p_path[i].val == self.q_path[i].val:
                ans = self.p_path[i]
        
        return ans



[3,5,1,6,2,0,8,null,null,7,4]
5
1
[1]
1
1
[]
0
1
[3,5,1,6,2,0,8,null,null,7,4]
5
4
[3,5,1,6,2,0,8,null,null,7,4]
3
0
[1,2]
2
1