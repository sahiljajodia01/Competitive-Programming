
def prettyPrint(A):
    n = 1 + 2 * (A-1)

    L = 0
    R = n-1
    T = 0
    B = n-1

    a = []

    for i in range(n):
        temp = []
        for i in range(n):
            temp.append(0)

        a.append(temp)

    count = A
    while L <= R and T <= B:
        for i in range(L, R+1):
            a[T][i] = count
            a[B][i] = count
        
        for i in range(T, B+1):
            a[i][L] = count
            a[i][R] = count

        L += 1
        R -= 1
        T += 1
        B -= 1

        count -= 1

    print(a)

prettyPrint(1)