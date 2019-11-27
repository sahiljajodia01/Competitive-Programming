# https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/627/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


######### Level order traversal approach. Checking if the elements at each level are in palindromic order ##############
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root:
#             level = [root]
#         else:
#             level = []
#         ans = []
#         while level != []:
#             queue = []
#             temp = []
            
#             for i in range(len(level)):
#                 if level[i] != None:
#                     temp.append(level[i].val)
#                     if level[i].left:
#                         queue.append(level[i].left)
#                     else:
#                         queue.append(None)

#                     if level[i].right:
#                         queue.append(level[i].right)
#                     else:
#                         queue.append(None)
#                 else:
#                     temp.append(None)
                    
#             level = queue
#             ans.append(temp)
            
#         for i in ans:
#             if i == i[::-1]:
#                 continue
#             else:
#                 return False
            
#         return True



############# Iterative Approach ###############
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         queue = []
        
#         queue.append(root)
#         queue.append(root)
        
#         while queue != []:
#             node1 = queue.pop(0)
#             node2 = queue.pop(0)
            
#             if node1 == None and node2 == None:
#                 continue
#             if node1 == None or node2 == None:
#                 return False
#             if node1.val != node2.val:
#                 return False
            
#             queue.append(node1.left)
#             queue.append(node2.right)
#             queue.append(node1.right)
#             queue.append(node2.left)
            
#         return True


############## Recursive Approach ################
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def symmetric(node1, node2):
#             if node1 == None and node2 == None:
#                 return True
#             if node1 == None or node2 == None:
#                 return False
#             if node1.val != node2.val:
#                 return False
            
#             ans1 = symmetric(node1.left, node2.right)
#             ans2 = symmetric(node1.right, node2.left)
            
#             if ans1 == False or ans2 == False:
#                 return False
#             else:
#                 return True
                    
#         return symmetric(root, root)