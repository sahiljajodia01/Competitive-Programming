def findMinXor(A):
    A = sorted(A)
    min_ = 9999999999
    for i in range(1, len(A)):
        if A[i] ^ A[i-1] < min_:
            min_ = A[i] ^ A[i-1]
        
    return min_


ans = findMinXor([0, 4, 7, 9])
print(ans)