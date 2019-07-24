import math

def find_prime(A):
    flag = 0
    if A == 1:
        return False
    for i in range(2, int(math.sqrt(A)) + 1):
        if A%i == 0:
            flag = 1
            break
        
    if flag == 0:
        return True
    else:
        return False

def primesum(A):
    for count in range(2, A+1):
        if find_prime(count):
            if find_prime(A - count):
                ans = [count, A-count]
                break
    
    # sorted_d = sorted(d.keys())

    # for i in sorted_d:
    #     if A-i in  d.keys():
    #         ans = [i, A-i]
    #         break

    print(ans)


primesum(16777214)