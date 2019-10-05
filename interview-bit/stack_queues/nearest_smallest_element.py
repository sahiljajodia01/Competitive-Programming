import pysnooper

def prevSmaller(A):
    s = []
    s.append(A[0])
    ans = [-1]
    for i in range(1, len(A)):
        while len(s) != 0:
            if A[i] > s[-1]:
                ans.append(s[-1])
                s.append(A[i])
                break
            else:
                s.pop()

        if len(s) == 0:
            s.append(A[i])
            ans.append(-1)

        
    print(ans)


prevSmaller([4, 5, 2, 10, 8])
prevSmaller([3, 2, 1])
prevSmaller([2, 10, 15, 100])
prevSmaller([1])
prevSmaller([3, 1, 2, 5])
prevSmaller([ 34, 35, 27, 42, 5, 28, 39, 20, 28 ])