# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


####### Similar to inorder traversal and just checking the kth smallest with an if condition #######
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums = []
        if root:
            stack = [root]
        else:
            stack = []

        while stack != []:
            ele = stack[-1]
            while ele.left != None:
                parent = ele
                stack.append(ele.left)
                ele = ele.left
                parent.left = None
            
            ele = stack.pop()
            nums.append(ele.val)
            
            if len(nums) == k:
                return nums[-1]
            
            if ele.right:
                stack.append(ele.right)
        
        return nums