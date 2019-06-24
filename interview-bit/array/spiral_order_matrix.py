# Not completed till now


import pysnooper

@pysnooper.snoop()
def generateMatrix(A):
    i = 0
    j = 0

    ans = []
    for i in range(A):
        temp = []
        for j in range(A):
            temp.append(0)

        ans.append(temp)
    i = 0
    j = 0
    count = 2
    m = A-1
    n = A-1
    count2 = 2

    num = 1
    while i != 1 and j != 1:
        if count % 2 == 0:
            if count % 4 == 0:
                while j != m-1:
                    ans[i][j] = num
                    num += 1
                    j -= 1
                j += 1
                m = A - 1 - m
                i -= 1
                count += 1
            else:
                while j != m+1:
                    ans[i][j] = num
                    num += 1
                    j += 1
                j -= 1
                m = A - 1 - m
                i += 1
                count += 1
        else:
            if count2 % 2 == 0:
                while i != n+1:
                    ans[i][j] = num
                    num += 1
                    i += 1
                i -= 1
                n = A  - 1 - n + 1
                count += 1
                count2 += 1
            else:
                while i != n-1:
                    ans[i][j] = num
                    num += 1
                    i -= 1
                i += 1
                n = A - 1 - n
                count += 1
                count2 += 1
    
    print(ans)

generateMatrix(3)