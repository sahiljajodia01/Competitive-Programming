def removeDuplicates(A):
    count = 0

    for i in range(0, len(A) - 1):
        if A[i+1] != A[i]:
            A[count] = A[i]
            count += 1

    A[count] = A[len(A) - 1]
    count += 1

    print(count)


removeDuplicates([1, 2, 2, 2, 4, 10, 10, 20])