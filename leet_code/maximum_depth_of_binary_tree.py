# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        max_depth = depth
        
        def check(root, depth, max_depth):
            if root == None:
                if max_depth < depth:
                    max_depth = depth
            
                return max_depth
            
            left = check(root.left, depth + 1, max_depth)
            right = check(root.right, depth + 1, max_depth)
            
            return max(left, right)
            
        return check(root, depth, max_depth)