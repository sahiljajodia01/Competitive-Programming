try:
    t = int(input())


    while t > 0:
        N, S = list(map(int, input().split(" ")))

        P = list(map(int, input().split(" ")))
        P_type = list(map(int, input().split(" ")))

        d = {0: [], 1: []}
        for i in range(len(P)):
            d[P_type[i]].append(P[i])

        # print(d)
        final = S + min(d[0]) + min(d[1])

        if final <= 100:
            print("yes")
        else:
            print("no")
        t -= 1
except:
    pass