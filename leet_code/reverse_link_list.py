# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


################# Iterative Solution ################
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_ptr = None
        next_ptr = None
        
        current = head
        
        while current != None:
            next_ptr = current.next
            current.next = prev_ptr
            prev_ptr = current
            current = next_ptr
            
        return prev_ptr