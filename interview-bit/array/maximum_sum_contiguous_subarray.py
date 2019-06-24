import pysnooper

@pysnooper.snoop()
def maxSubArray(A):
    if max(A) < 0:
        return max(A)
    sum_ = 0
    ans = 0
    
    for i in A:
        if i+sum_ >= 0:
            sum_ += i
            if sum_ > ans:
                ans = sum_
        else:
            sum_ = 0
    
    print(ans)

a = [-2,1,-3,4,-1,2,1,-5,4]


maxSubArray(a)