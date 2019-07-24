def numberToTitle(A):
    string = ''
    while A != 0:
        temp = (A-1)%26
        char = chr(temp + 65)
        string += char
        A = (A-1)//26

    print(string[::-1])

numberToTitle(29)
