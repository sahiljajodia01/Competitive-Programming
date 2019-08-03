def romanToInt(A):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = d[A[-1]]
    for i in range(len(A)-2, -1, -1):
        if d[A[i]] >= d[A[i+1]]:
            count += d[A[i]]
        else:
            count -= d[A[i]]
    
    return count

ans = romanToInt("XIV")
print(ans)

ans = romanToInt("MDCCCIV")
print(ans)