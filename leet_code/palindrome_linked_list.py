# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

############ In place solution. Reversing 2nd half of list and checking with first half ###########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        middle = head
        length = 0
        while middle != None:
            middle = middle.next
            length += 1
        
        middle = head
        if length % 2 == 0:
            for i in range(1, length//2 + 1):
                middle = middle.next;
        else:
            for i in range(1, length//2 + 2):
                middle = middle.next;
        
        prev = None
        next_ptr = None
        
        while middle != None:
            next_ptr = middle.next
            middle.next = prev
            prev = middle
            middle = next_ptr
            
        middle = prev
        start = head
        
        while middle != None:
            print(middle.val, start.val)
            if middle.val != start.val:
                return False
            
            middle = middle.next
            start = start.next
        
        return True