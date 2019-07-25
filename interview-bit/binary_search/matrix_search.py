def searchMatrix(A, B):
    N = len(A)
    M = len(A[0])
    
    row = 0
    column = M-1

    while row <= N-1 and column >= 0:
        if A[row][column] == B:
            print("True")
            break
        elif A[row][column] > B:
            column -= 1
        else:
            row += 1

searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30 , 34, 50]], 303)
