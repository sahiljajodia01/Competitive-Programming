# https://codeforces.com/contest/1352/problem/A

t = int(input())

for i in range(t):
    num = int(input())

    copy = num
    count = 0
    ans = []
    while copy > 0:
        digit = copy % 10

        if digit != 0:
            ans.append((digit * (10**(count))))
        
        count += 1
        copy = copy//10

    print(len(ans))

    for i in range(len(ans)):
        print(ans[i], end=' ')

    print()
