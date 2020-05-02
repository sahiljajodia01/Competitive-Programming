# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/

####### Using 2 pointer approach. First pointer at normal speed. Second pointer at 2x speed.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        first = head
        second = head
        
        while second != None and second.next != None:
            first = first.next
            second = second.next.next
        
        return first