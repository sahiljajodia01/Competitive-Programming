def dec_to_bin(n):
    b = ''

    if n == 0:
        return '0'
    while n > 0:
        b += str(n % 2)
        n = n//2
    
    return b[::-1]

def numSetBits(A):
    ###### Unoptimized answer #########
    A = dec_to_bin(A)
    count = 0
    for i in A:
        if i == '1':
            count += 1
    
    return count


ans = numSetBits(2)
print(ans)