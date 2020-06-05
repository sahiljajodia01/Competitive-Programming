# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {None:None}
        
        copy = head
        
        root = None
        ans = None
        while copy != None:
            if root:
                root.next = Node(copy.val)
                root = root.next
            else:
                root = Node(copy.val)
                ans = root
            
            d[copy] = root
            copy = copy.next
            
        while head != None:
            d[head].random = d[head.random]
            head = head.next
        
        return ans