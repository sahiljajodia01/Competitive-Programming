import pysnooper

@pysnooper.snoop()
def merge(A, B):
    c = []

    c1 , c2 = 0, 0

    while c1 < len(A) and c2 < len(B):
        if A[c1] <= B[c2]:
            c.append(A[c1])
            c1 += 1
        else:
            c.append(B[c2])
            c2 += 1
    
    if c1 < len(A):
        c.append(A[c1])
        c1 += 1
    
    if c2 < len(B):
        c.append(B[c2])
        c2 += 1

    print(c)


merge([-4, 3], [-2, -2])
