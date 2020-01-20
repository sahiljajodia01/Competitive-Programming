# https://leetcode.com/contest/weekly-contest-172/problems/delete-leaves-with-a-given-value/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def solve(root, target, parent, changed):
            # print(root)
            if root.val == target and root.left == None and root.right == None:
                # print("Changing, root: ", root)
                # print("Parent: ", parent)
                if root == parent:
                    root = None
                else:
                    if root == parent.left:
                        parent.left = root.left
                    else:
                        parent.right = root.right
                    changed[0] = True
            else:
                if root.left:
                    solve(root.left, target, root, changed)
                
                if root.right:
                    solve(root.right, target, root, changed)
        
        if root == None:
            return None
        else:
            while True:
                # print("Times")
                changed = [False]
                copy = root
                solve(root, target, root, changed)
                if changed[0] == False or root == None:
                    break
                    
            if root.val == target and root.left == None and root.right == None:
                root = None
            
            return root