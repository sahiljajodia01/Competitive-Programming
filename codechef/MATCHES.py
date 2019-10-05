tc = int(input())

d = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6
}

for _ in range(tc):
    a, b = list(map(int, input().split(" ")))

    total = str(a+b)

    sum_ = 0

    for i in total:
        sum_ += d[i]

    print(sum_)
