# Optimized O(n) solution is not completed. This is O(n^2) solution 


import pysnooper

@pysnooper.snoop()
def maxArr(A):
    sum_ = 0
    B = A.sort()

    m = 0
    n = len(B) - 1

    ans = abs(B[m] - B[n]) + abs(A.index(B[m]) - A.index(B[n]))

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            ans = abs(A[i] - A[j]) + abs(i - j)
            if ans > sum_:
                sum_ = ans
    
    print(sum_)


A = [0, 2, -1, 5, -4]

maxArr(A)