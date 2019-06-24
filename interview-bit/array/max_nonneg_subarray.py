import pysnooper

@pysnooper.snoop()
def maxset(A):
    arr = []
    temp = []
    for i in range(len(A)):
        if A[i] >= 0:
            temp.append(A[i])
        else:
            if len(temp) > 0:
                arr.append(temp)
                temp = []
    if len(temp) > 0:
        arr.append(temp)
        temp = []
    
    if len(arr) == 0:
        return arr
    sum_arr = []
    length = []
    for i in arr:
        ans = sum(i)
        ans2 = len(i)
        sum_arr.append(ans)
        length.append(ans2)

    indexes = []

    sum_ = 0
    for i in sum_arr:
        if i > sum_:
            sum_ = i
    
    for i in range(len(sum_arr)):
        if sum_arr[i] == sum_:
            indexes.append(i)
    len_indexes = []
    if len(indexes) == 1:
        print(arr[indexes[0]])
    else:
        final_index = 0
        len_index = length[indexes[0]]
        for i in range(1, len(indexes)):
            if length[indexes[i]] > len_index:
                final_index = i
        print(arr[final_index])
    # print(arr)


A = [-1, -1, -1]
maxset(A)