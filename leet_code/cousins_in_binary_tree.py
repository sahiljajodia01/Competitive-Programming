# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/

###### Recursive path find solution. Getting the depth and parent of both nodes. ######
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        x_val = [None, 0]
        y_val = [None, 0]
        def solve(root, x, y, depth, parent, x_val, y_val):
            if root.val == x:
                if parent:
                    x_val[0] = parent.val
                x_val[1] = depth
                return
            elif root.val == y:
                if parent:
                    y_val[0] = parent.val
                y_val[1] = depth
                return
            elif root.left == None and root.right == None:
                return
            
            if root.left:
                solve(root.left, x, y, depth+1, root, x_val, y_val)
            
            if root.right:
                solve(root.right, x, y, depth+1, root, x_val, y_val)
        
    
        solve(root, x, y, 0, None, x_val, y_val)

        if y_val[1] == x_val[1] and y_val[0] != x_val[0]:
            return True

        return False