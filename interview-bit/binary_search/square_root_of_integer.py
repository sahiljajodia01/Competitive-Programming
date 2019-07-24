import math
# import pysnooper


# @pysnooper.snoop()
def sqrt(A):
    low, high = 1, A

    root = 0

    while low <= high:
        mid = (low+high)//2

        if mid*mid == A:
            root = mid
            break
        elif mid*mid < A:
            root = mid
            low = mid+1
        else:
            high = mid-1

        
    root = math.floor(root)

    print(root)


sqrt(15)