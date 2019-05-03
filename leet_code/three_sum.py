import pysnooper

inp = input("Enter the numbers: ").split(" ")

inp = [int(i) for i in inp]


dic = {}

for i in inp:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

# @pysnooper.snoop()
def main():
    sol = []
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            temp1 = inp[i]
            temp2 = inp[j]

            f = -1 * (temp1 + temp2)

            if f in dic.keys():
                if temp1 == f and temp2 == f:
                    if dic[f] < 3:
                        continue
                elif (temp1 == f and temp2 != f) or (temp2 == f and temp1 != f):
                    if dic[f] < 2:
                        continue
                arr = [temp1, temp2, f]
                arr.sort()

                
                sol.append(arr)
    print(sol)

    print(list(map(list, list(set(map(tuple, sol))))))

main()
