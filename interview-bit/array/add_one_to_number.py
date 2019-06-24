def plusOne(A):
    A.insert(0, 0)
    for i in range(len(A) - 1, -1, -1):
        A[i] = (A[i] + 1)%10
        
        if A[i] == 0:
            continue
        else:
            break
        
    for i in range(0, len(A)):
        if A[i] == 0:
            A.pop(0)
        else:
            break
            
    return A