def lengthOfLastWord(A):
    temp = []
    flag = 0
    for i in range(len(A) - 1, -1, -1):
        if flag == 0:
            if A[i] != ' ':
                temp.append(A[i])
                flag = 1
            else:
                continue
        else:
            if A[i] != ' ':
                temp.append(A[i])
            else:
                break

    return len(temp)


ans = lengthOfLastWord("Hello World  ")
print(ans)
                