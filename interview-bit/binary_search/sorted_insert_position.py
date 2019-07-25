def searchInsert(A, B):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low+high)//2
        if A[mid] == B:
            return mid
        elif A[mid] > B:
            high = mid-1
        else:
            low = mid+1

    if A[mid] > B:
        return mid
    else:
        return mid+1


ans = searchInsert([1, 3, 5, 6], 0)
print(ans)