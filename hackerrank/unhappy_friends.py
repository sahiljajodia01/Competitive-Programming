a, b = input().split()

a, b = int(a), int(b)

string = input()
friend_arr = ['' for i in range(b)]
for i in string:
    flag = 0
    for j in range(len(friend_arr)):
        if i in friend_arr[j]:
            continue
        else:
            friend_arr[j] += i
            flag = 1
            break
    
    if flag == 0:
        break

if flag == 0:
    print("NO")
else:
    print("YES")