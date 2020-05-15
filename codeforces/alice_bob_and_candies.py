# https://codeforces.com/contest/1352/problem/D

t = int(input())

while t > 0:
    t -= 1

    n = int(input())

    candies = list(map(int, input().split(" ")))

    p1 = 0
    p2 = n-1

    flag = 1
    prev = 0
    sum_a = 0
    sum_b = 0
    moves = 0
    while p1 <= p2:
        moves += 1
        if flag == 1:
            temp = 0
            while temp <= prev and p1 <= p2:
                temp += candies[p1]
                p1 += 1
            
            prev = temp
            sum_a += prev
        else:
            temp = 0
            while temp <= prev and p1 <= p2:
                temp += candies[p2]
                p2 -= 1
            
            prev = temp
            sum_b += prev
        
        flag *= -1
    
    print(moves, sum_a, sum_b)