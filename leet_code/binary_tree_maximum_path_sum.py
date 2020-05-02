# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_ = -2147483648
        def inorder(root):
            if root == None:
                return None

            left = inorder(root.left)
            current = root.val
            right = inorder(root.right)
            # print(left, current, right)
            if left == None and right != None:
                self.max_ = max(self.max_, current, right, right+current)
                left = 0
            elif right == None and left != None:
                self.max_ = max(self.max_, current, left, left+current)
                right = 0
            elif left == None and right == None:
                self.max_ = max(self.max_, current)
                left, right = 0, 0
            else:
                self.max_ = max(self.max_, max(left, right, current, left+current, right+current, left+right+current))
            return max(current, left+current, right+current)

        ans = inorder(root)
        return self.max_


[1,2,3]
[-10,9,20,null,null,15,7]
[-10,9,20,33, -11,15,7, null, -15, 25, null, 30, -17, 2, 5, null, null, null, null, 19, 3, null, -8]
[-10]
[-10, null, 2, 3]
[-10, -9, -12]
[]
[1, 2]
[1,-2,-3,1,3,-2,null,-1]
[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]