# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


######### My solution. Not a very elegant one. Time complexity is O(n) but it still is lot slower #########
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        counter = 10
        while l1 != None:
            data = l1.val
            num1 += str(data)
            l1 = l1.next

        while l2 != None:
            data = l2.val
            num2 += str(data)
            l2 = l2.next
            
        num1_rev, num2_rev = num1[::-1], num2[::-1]
        
        total = eval(num1_rev + '+' + num2_rev)
        total = str(total)[::-1]
        head = None
        copy = head
        
        for i in range(len(total)):
            if head == None:
                head = ListNode(int(total[i]))
                copy = head
            else:
                head.next = ListNode(int(total[i]))
                head = head.next
        
        return copy


####### Addition of two numbers solution. ########
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = None
        copy = head
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                num1 = 0
            else:   
                num1 = l1.val
                l1 = l1.next
            
            if l2 == None:
                num2 = 0
            else:
                num2 = l2.val
                l2 = l2.next
            
            total = num1 + num2 + carry
            
            if total > 9:
                carry = 1
                total = total % 10
            else:
                carry = 0
            
            if head == None:
                head = ListNode(total)
                copy = head
            else:
                head.next = ListNode(total)
                head = head.next
            
        
        if carry == 1:
            if head == None:
                head = ListNode(1)
                copy = head
            else:
                head.next = ListNode(1)
                head = head.next
        
        return copy