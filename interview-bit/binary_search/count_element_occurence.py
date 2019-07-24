def findCount(A, B):
    size = len(A)

    low, high = 0, size-1
    count = 0
    while low <= high:
        mid = (low + high)//2

        if B == A[mid]:
            print("Inside if")
            count += 1
            for i in range(mid+1, high+1):
                if A[i] == B:
                    count += 1
                else:
                    break
            
            for i in range(mid-1, low-1, -1):
                if A[i] == B:
                    count += 1
                else:
                    break
            break
        elif A[mid] < B:
            print("Inisde elif")
            low = mid+1
        else:
            print("Inisde else")
            high = mid-1

    print(count)


findCount([5, 7, 7, 8, 8, 10], 8)
