# https://codeforces.com/contest/1352/problem/F

t = int(input())

while t > 0:
    t -= 1

    c, b, a = list(map(int, input().split(" ")))

    s = ""
    if a > 0:
        for i in range(a+1):
            s += "1"
    else:
        if b != 0:
            s += "1"
        else:
            s += "0"
    
    zero = 1
    for i in range(b):
        if zero == 1:
            if c > 0:
                s += "0"
                while c != 0:
                    s += "0"
                    c -= 1
            else:
                s += "0"
        else:
            s += "1"

        zero *= -1

    for i in range(c):
        s += "0"

    print(s)