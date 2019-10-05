def evalRPN(A):
    s = []

    for i in range(len(A)):
        if A[i] == '+' or A[i] == '-' or A[i] == '*' or A[i] == '/':
            pass
        else:
            s.append(A[i])

        