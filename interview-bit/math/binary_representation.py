def binary(A):
    arr = []
    while A >= 1:
        if A % 2 == 0:
            arr.append(0)
        else:
            arr.append(1)

        A = A//2

    print(arr[::-1])


ip = int(input())
binary(ip)
