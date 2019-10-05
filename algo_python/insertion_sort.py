def insertion_sort(a):
    for i in range(1, len(a)):
        curr = a[i]
        idx = i

        while idx > 0 and curr < a[idx-1]:
            a[idx] = a[idx-1]
            idx -= 1
        
        a[idx] = curr

    return a

arr = [43, 348, 348, 38, 49, 50, 595, 328, 398, 5894]
print(arr)
print(insertion_sort(arr))