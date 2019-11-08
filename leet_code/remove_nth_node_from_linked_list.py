# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


############### Two pass approach #####################
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        
        l = head
        
        while l != None:
            length += 1
            l = l.next
        
        print(length)
        length_nodes = length - n
        l = head
        if n != length:
            while l.next != None:
                print(l.val)
                if length_nodes == 1:
                    l.next = l.next.next
                    break
                length_nodes -= 1
                l = l.next
        else:
            head = head.next

        return head


################ One pass approach - Here we'll take two pointers. One at Null and other at position ##############
################ n from the beginning. Then we continue till first reaches till the end and then we  ##############
################ delete the node #############

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        initial = ListNode(0)
        initial.next = head
        first = initial
        second = initial
        for i in range(0, n+1):
            first = first.next
        
        while first != None:
            first = first.next
            second = second.next
            
        second.next = second.next.next

        return initial.next