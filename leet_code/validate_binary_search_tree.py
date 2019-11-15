# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        else:
            return self.check(root)
        
    def check(self, root: TreeNode, minimum=float('-inf'), maximum=float('inf')) -> bool:
        if root == None:
            return True
        
        if root.val <= minimum or root.val >= maximum:
            return False
        
        return self.check(root.left, minimum, root.val) and self.check(root.right, root.val, maximum)