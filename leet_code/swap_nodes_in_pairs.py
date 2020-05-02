# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/



######### First storing the next node of head. Then Recursively assigning head.next = head.next.next. Then the
######### next of the above stored next is the head. And finally return next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def solve(head):
            # print(head)
            if head == None or head.next == None:
                return head
            else:
                next_ = head.next
                head.next = solve(head.next.next)
                next_.next = head
                
                return next_
        
        return solve(head)