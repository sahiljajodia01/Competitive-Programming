def solve(A):
    d = {}
    for i in A:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1

    
    for i in range(len(A)):
        for j in range(i+1, len(A)):
