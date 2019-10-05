# https://www.interviewbit.com/problems/intersection-of-linked-lists/

def getIntersectionNode(self, A, B):
    len_a = 0
    len_b = 0
    currA = A
    currB = B
    while currA != None:
        len_a += 1
        currA = currA.next
        
    while currB != None:
        len_b += 1
        currB = currB.next
        
    
    if len_a > len_b:
        for _ in range(0, len_a - len_b):
            A = A.next
    elif len_b > len_a:
        for _ in range(0, len_b - len_a):
            B = B.next
            
            
    while A != None:
        if A == B:
            return A
        else:
            A = A.next
            B = B.next
            
    return None