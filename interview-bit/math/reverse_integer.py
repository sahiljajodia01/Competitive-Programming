import pysnooper

@pysnooper.snoop()
def reverse(A):
    reverse = 0
    flag = 0
    if A < 0:
        A = A * -1
        flag = 1
        
    copy = A
    prev_reverse = 0
    while copy != 0:
        temp = copy % 10
        reverse = reverse * 10 + temp
        
        # if (reverse >= 2147483647 or reverse <= -2147483648): 
        #     reverse = 0
        
        if (reverse - temp)//10 != prev_reverse:
            return 0
        
        prev_reverse = reverse
        copy = copy//10
    
    if flag == 1:
        reverse = reverse * -1
        
    return reverse

ans = reverse(2147483647)
print(ans)