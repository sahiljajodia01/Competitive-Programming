# https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/628/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            level = [root]
        else:
            level = []
        ans = []    
        while len(level) != 0:
            arr = []
            temp = []
            for i in range(len(level)):
                temp.append(level[i].val)
                if level[i].left:
                    arr.append(level[i].left)
                
                if level[i].right:
                    arr.append(level[i].right)
                    
            level = arr
            ans.append(temp)
        
        return ans