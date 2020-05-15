# https://codeforces.com/contest/1352/problem/B

t = int(input())

while t > 0:
    # print(t)
    n, k = list(map(int, input().split(" ")))

    if k > n:
        print("NO")
    elif n % 2 == 0:
        if k % 2 == 0:
            print("YES")
            sum_ = 0
            for i in range(k-1):
                print("1", end=" ")
                sum_ += 1

            print(n-sum_)
        else:
            if k > n//2:
                print("NO")
            else:
                print("YES")
                sum_ = 0
                for i in range(k-1):
                    print("2", end=" ")
                    sum_ += 2
            
                print(n-sum_)
    else:
        if k % 2 != 0:
            print("YES")
            sum_ = 0
            for i in range(k-1):
                print("1", end=" ")
                sum_ += 1

            print(n-sum_)
        else:
            print("NO")

    t -= 1