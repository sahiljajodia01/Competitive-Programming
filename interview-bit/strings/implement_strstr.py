import pysnooper

@pysnooper.snoop()
def strStr(A, B):
    counter = 0
    index = -1

    if len(B) == 0 or len(A) == 0:
        return index
    for i in range(len(A)):
        if A[i] == B[counter]:
            if i + len(B) <= len(A):
                for j in range(i, i + len(B)):
                    if A[j] == B[counter]:
                        counter += 1
                    else:
                        counter = 0
                        break
                if counter  == len(B):
                    index = i
                    break

    
    return index


ans = strStr('b', 'b')
print(ans)
    