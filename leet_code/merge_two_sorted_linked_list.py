# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        initial = ListNode(0)
        count = 0
        while l1 != None and l2 != None:
            first = l1.val
            second = l2.val
            if first <= second:
                if count == 0:
                    l = ListNode(first)
                    initial.next = l
                else:
                    node = ListNode(first)
                    l.next = node
                    l = l.next
                l1 = l1.next
            else:
                if count == 0:
                    l = ListNode(second)
                    initial.next = l
                else:
                    node = ListNode(second)
                    l.next = node
                    l = l.next
                l2 = l2.next
                
            count += 1
            
        ptr = initial
        
        while ptr.next != None:
            ptr = ptr.next
        
        if l1 == None:
            while l2 != None:
                val = l2.val
                node = ListNode(val)
                ptr.next = node
                ptr = ptr.next
                l2 = l2.next
        
        if l2 == None:
            while l1 != None:
                val = l1.val
                node = ListNode(val)
                ptr.next = node
                ptr = ptr.next
                l1 = l1.next
        return initial.next