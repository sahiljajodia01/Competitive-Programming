import re

def isPalindrome(A):
    A = re.sub('[\W_]+', '', A).lower()
    print(A)
    flag = 0
    for i in range(0, len(A)//2):
        print("A[first]: ", A[i])
        print("A[last]: ", A[len(A) - i - 1])
        if A[i] != A[len(A) - i - 1]:
            flag = 1
            break
    
    if flag == 0:
        print("Palindrome")
    else:
        print("Not Palindrome")
        
    ######  Simple solution without implementing actual palindome logic ######
    # if A == A[::-1]:
    #     return 1
    # else:
    #     return 0

isPalindrome("A man, a plan, a canal: Panama")
isPalindrome("race a car")