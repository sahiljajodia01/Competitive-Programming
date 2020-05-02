# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


###### My solution using BFS approach. Slower because a lot of work is repeated
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def find_depth(ele):
            depth = 0
            if ele:
                level = [ele]
            else:
                level = []

            while level != []:
                depth += 1
                arr = []

                for i in range(len(level)):
                    if level[i].left:
                        arr.append(level[i].left)

                    if level[i].right:
                        arr.append(level[i].right)
                level = arr

            return depth
            
            
        
        if not root:
            return 0
        
        q = [root]
        max_ = 0
        while q != []:
            ele = q.pop(0)
            # print("Ele: ", ele.val)
            
            left = 0
            if ele.left:
                left = find_depth(ele.left)
                q.append(ele.left)
            
            right = 0
            if ele.right:
                right = find_depth(ele.right)
                q.append(ele.right)
            # print("Left: ", left, ", Right: ", right)
            length = left+right
            
            if length > max_:
                max_ = length
        
        return max_


###### DFS solution that I saw in discussions. Short, simple and sweet solution. O(n) time complexity
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_ = 0
        def dfs_depth(ele):
            
            if not ele:
                return 0
            
            left = dfs_depth(ele.left)
            right = dfs_depth(ele.right)
            
            self.max_ = max(self.max_, left+right)
            
            return max(left, right) + 1
        
        ele = dfs_depth(root)
        return self.max_