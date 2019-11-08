# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

####### Two pointer approach with constant memory ########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        first = head
        second = head
        
        flag = 0
        while first != None and second.next != None and second.next.next != None:    
            first = first.next
            second = second.next.next
            
            if first == second:
                flag = 1
                break
            
        if flag == 1:
            return True
        else:
            return False