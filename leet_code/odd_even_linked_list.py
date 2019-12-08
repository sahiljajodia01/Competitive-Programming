# https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


######## Linear time and Constant space solution #########
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        first_even = None
        ptr = head
        count = 1
        prev_odd = None
        prev_even = None
        while ptr != None:
            print(ptr.val)
            if count % 2 != 0 and prev_odd != None:
                prev_odd.next = ptr
                prev_odd = ptr
            
            if count % 2 != 0 and prev_odd == None:
                prev_odd = ptr
                
            if count % 2 == 0 and prev_even != None:
                prev_even.next = ptr
                prev_even = ptr
            
            if count % 2 == 0 and prev_even == None:
                prev_even = ptr
                first_even = ptr

            ptr = ptr.next
            count += 1
        
        if count % 2 == 0 and prev_even != None:
            prev_even.next = None
        
        if prev_odd != None:
            prev_odd.next = first_even
        
        return head


######### A very concise but non trivial solution from leetcode solutions ########
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        ptr_odd = head
        ptr_even = head.next
        first_even = ptr_even
        
        while ptr_even != None and ptr_even.next != None:
            ptr_odd.next = ptr_even.next
            ptr_odd = ptr_odd.next
            ptr_even.next = ptr_odd.next
            ptr_even = ptr_even.next
            
        ptr_odd.next = first_even
        
        return head