# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA = headA
        ptrB = headB
        
        lengthA, lengthB = 0, 0
        
        while ptrA != None:
            lengthA += 1
            ptrA = ptrA.next
            
        while ptrB != None:
            lengthB += 1
            ptrB = ptrB.next
        

        while True:
            if lengthA == lengthB:
                break
            
            if lengthA > lengthB:
                headA = headA.next
                lengthA -= 1
            else:
                headB = headB.next
                lengthB -= 1
        
        while headA != None:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
        
        return None