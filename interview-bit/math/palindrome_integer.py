def palindrome(A):
    copy = A
    reverse = 0
    while copy != 0:
        temp = copy % 10

        reverse = reverse * 10 + temp
        copy = copy//10

    if reverse == A:
        print("True")
    else:
        print("False")

palindrome(123)