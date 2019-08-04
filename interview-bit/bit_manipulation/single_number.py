def singleNumber(A):
    xor_sum = 0 ^ A[0]
    for i in range(1, len(A)):
        xor_sum ^= A[i]

    
    return xor_sum


ans = singleNumber([1, 2, 2, 3, 1])
print(ans)