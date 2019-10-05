def combine(a, b):
    c = []
    a_idx, b_idx = 0, 0

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1

    
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])

    return c

def merge_sort(a):
    if len(a) <= 1:
        return a
    
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])

    return combine(left, right)


arr = [43, 348, 348, 38, 49, 50, 595, 328, 398, 5894]
print(arr)
print(merge_sort(arr))