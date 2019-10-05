import pysnooper

# @pysnooper.snoop()
def solve(A, B, C):
    z = [-1, -1, -1]
    a = 0
    b = 0
    c = 0

    z[0] = A[a]
    z[1] = B[b]
    z[2] = C[c]

    ans = abs(max(z) - min(z))

    min_index = z.index(min(z))

    if min_index == 0:
        a += 1
    elif min_index == 1:
        b += 1
    else:
        c += 1

    while True:
        if len(A) == 1 or len(B) == 1 or len(C) == 1:
            break
        
        if a == len(A) or b == len(B) or c == len(C):
            break
        z[0] = A[a]
        z[1] = B[b]
        z[2] = C[c]

        new_ans = abs(max(z) - min(z))

        if new_ans <= ans:
            ans = new_ans

        min_index = z.index(min(z))

        if min_index == 0:
            a += 1
        elif min_index == 1:
            b += 1
        else:
            c += 1
    
    print(z)
    print(ans)


solve([ 1, 4, 5, 8, 10 ], [ 6, 9, 15 ], [ 2, 3, 6, 6 ])
solve([-1], [-2], [-3])
solve([ 1, 4, 5, 8, 10 ], [ 6, 9, 10 ], [ 2, 3, 6, 10 ])