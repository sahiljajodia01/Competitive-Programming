def intersect(A, B):
    c1 = 0
    c2 = 0
    c = []
    while c1 < len(A) and c2 < len(B):
        if A[c1] < B[c2]:
            c1 += 1
        elif A[c1] > B[c2]:
            c2 += 1
        else:
            c.append(A[c1])
            c1 += 1
            c2 += 1

    print(c)

intersect([1, 2, 3, 3, 4, 5, 6], [3, 3, 7])