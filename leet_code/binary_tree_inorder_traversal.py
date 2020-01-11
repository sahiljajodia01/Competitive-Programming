# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


######## Trivial Recursive solution ########
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root, nums):
            if root == None:
                return
            inorder(root.left, nums)
            nums.append(root.val)
            inorder(root.right, nums)
            
            return nums
        
        return inorder(root, [])



############ Iterative solution using stack ############
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nums = []
        if root:
            stack = [root]
        else:
            stack = []

        while stack != []:
            print(stack)
            ele = stack[-1]
            while ele.left != None:
                parent = ele
                stack.append(ele.left)
                ele = ele.left
                parent.left = None
            
            ele = stack.pop()
            nums.append(ele.val)
            
            if ele.right:
                stack.append(ele.right)
        
        return nums