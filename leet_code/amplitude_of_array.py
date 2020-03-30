def solution(A):
    if len(A) <= 3:
        return 0

    A = sorted(A)
    ans = min((A[len(A)-4] - A[0]), (A[len(A)-3] - A[1]), (A[len(A)-2] - A[2]), (A[len(A)-1] - A[3]))

    return ans

arrays = [[-9, 8, -1], [14, 10, 5, 1, 0], [11, 0, -6, -1, -3, 5], [10, 10, -6, 2, -3, 10], [8, -1, 4, 3, 5, -1]]
for array in arrays:
    ans = solution(array)
    print(ans)