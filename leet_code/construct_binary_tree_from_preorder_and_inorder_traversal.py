# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


######### Kinda slow iterative solution using hashmaps #########
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        head = None
        
        in_d = {}
        for i in range(len(inorder)):
            if inorder[i] not in in_d.keys():
                in_d[inorder[i]] = i
                        
        for i in range(len(preorder)):
            ele = preorder[i]
            ptr = head
            
            if head == None:
                head = TreeNode(ele)
                ptr = head
                print(ptr, "if")
            else:
                while True:
                    if in_d[ele] < in_d[ptr.val]:
                        if ptr.left != None:
                            ptr = ptr.left
                        else:
                            ptr.left = TreeNode(ele)
                            break
                    else:
                        if ptr.right != None:
                            ptr = ptr.right
                        else:
                            ptr.right = TreeNode(ele)
                            break
                print(ptr)
        return head



######## Recursive solution using deque for fast left pop #########
from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        
        def build_tree(preorder, inorder):
            if inorder:
                index = inorder.index(preorder.popleft())
                root = TreeNode(inorder[index])
                root.left = build_tree(preorder, inorder[:index])
                root.right = build_tree(preorder, inorder[(index+1):])
                return root
            
        return build_tree(preorder, inorder)