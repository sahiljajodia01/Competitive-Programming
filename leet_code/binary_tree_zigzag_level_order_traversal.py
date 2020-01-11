# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            level = [root]
        else:
            level = []
            
        ans = []
        reverse = -1
        while level != []:
            temp = []
            queue = []
            for i in level:
                temp.append(i.val)
                if i.left:
                    queue.append(i.left)
                
                if i.right:
                    queue.append(i.right)
            
            if reverse == 1:
                for i in range(len(temp)//2):
                    temp[i], temp[len(temp)-i-1] = temp[len(temp)-i-1], temp[i]
            
            reverse *= -1
            ans.append(temp)
            level = queue
        
        return ans