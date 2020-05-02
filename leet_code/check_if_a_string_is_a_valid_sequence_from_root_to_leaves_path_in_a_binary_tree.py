# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/


######### O(n) python backtracking solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def solve(root, arr, ans):
            # print(ans)
            if root.left == None and root.right == None:
                if ans == arr:
                    return True
                else:
                    return False
            
            
            left = False
            if root.left:
                ans.append(root.left.val)
                left = solve(root.left, arr, ans)
                ans.pop()
            right = False
            if root.right:
                ans.append(root.right.val)
                right = solve(root.right, arr, ans)
                ans.pop()
                
            if left or right:
                return True
            else:
                return False
        
        return solve(root, arr, [root.val])