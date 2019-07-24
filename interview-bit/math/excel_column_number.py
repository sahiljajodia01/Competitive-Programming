def titleToNumber(A):
    A = A[::-1]
    # print(A)
    sum_ = 0
    for i in range(len(A)):
        # print(A[i])
        num = ord(A[i]) - 64
        # print(num)
        sum_ += num * (26 ** i)

    print(sum_)


titleToNumber('A')