import re

def reverseWords(A):
    arr = re.split(r'[ ]+', A)

    arr = arr[::-1]

    output = ' '.join(arr)

    print(output)


reverseWords("the sky is blue")
reverseWords("this is ib")