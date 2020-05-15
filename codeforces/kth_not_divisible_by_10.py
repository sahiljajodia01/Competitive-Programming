# https://codeforces.com/contest/1352/problem/C

t = int(input())


while t > 0:
    t -= 1

    n, k = list(map(int, input().split(" ")))

    if n > k:
        print(k)
        continue

    initial = n-1
    copy = n
    diff = k - initial
    multiplier = diff//initial
    if diff % initial != 0:
        multiplier += 1
    # print(diff, multiplier)
    initial = initial + initial*multiplier
    copy = copy + copy*multiplier

    # while initial < k:
    #     initial += n-1
    #     copy += n

    copy = copy-1
    # print(initial, copy)
    print(copy - (initial-k))
