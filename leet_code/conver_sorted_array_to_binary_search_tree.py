# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.root = None
        def insert(root, val):
            if root == None:
                self.root = TreeNode(val)
            else:
                while True:
                    if val <= root.val:
                        if root.left:
                            root = root.left
                        else:
                            root.left = TreeNode(val)
                            break
                    else:
                        if root.right:
                            root = root.right
                        else:
                            root.right = TreeNode(val)
                            break
                        
        def sol(nums, beg, end):
            if beg <= end:
                mid = (beg+end+1)//2
                print(beg, end, mid)
                insert(self.root, nums[mid])
                sol(nums, beg, mid-1)
                sol(nums, mid+1, end)
        
        print(self.root)
        sol(nums, 0, len(nums)-1)
        print(self.root)
        return self.root