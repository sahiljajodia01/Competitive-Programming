t = int(input())

for z in range(t):
    inp = str(input())
    inp = inp.split()
    n = int(inp[0])
    p = int(inp[1])

    maxMod = n%(n // 2 + 1)
    if maxMod == 0:
        print(p*p*p)
    else:
        print((p-maxMod)*(p-maxMod) + (p-n)*(p-maxMod) + (p-n)*(p-n))