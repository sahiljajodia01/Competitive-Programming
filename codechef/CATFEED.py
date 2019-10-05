tc = int(input())

for _ in range(tc):
    n, m = list(map(int, input().split(" ")))
    order = list(map(int, input().split(" ")))

    # print(type(n))
    d = {}
    flag = 0
    for i in range(m):
        if (i+1) % n == 0:
            if order[i] in d.keys():
                d[order[i]] += 1
            else:
                d[order[i]] = 1
            
            # print(d)
            for key, value in d.items():
                if key != order[i]:
                    if value == d[order[i]]:
                        continue
                    else:
                        flag = 1
                        break
        else:
            if order[i] in d.keys():
                d[order[i]] += 1
            else:
                d[order[i]] = 1
            # print(d)


    if flag == 1:
        print("NO")
    else:
        print("YES")
