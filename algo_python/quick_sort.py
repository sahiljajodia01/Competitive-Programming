def partition(a, low, high):
    i = low-1
    pivot = a[high]

    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]

    return i+1


def quick_sort(a, low=0, high=None):
    if high == None:
        high = len(a) - 1

    if low < high:
        pivot = partition(a, low, high)
        a = quick_sort(a, low, pivot - 1)
        a = quick_sort(a, pivot + 1, high)
    
    return a


arr = [43, 348, 348, 38, 49, 50, 595, 328, 398, 5894]
print(arr)
print(quick_sort(arr))
