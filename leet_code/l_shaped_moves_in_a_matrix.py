

######## This is a non graph based approach. I dont know if this solution is completely right or not till now ########
def solution(a, b):
    matrix = []

    count = 0
    for i in range(8):
        temp = []
        for j in range(8):
            temp.append(count)
            count += 1
        
        matrix.append(temp)

    # print(matrix)

    current = a

    current_row = current // 8
    current_col = current%8
    final_row = b // 8
    final_col = b%8
    print(current_row, current_col)
    print(final_row, final_col)
    row_diff = abs(final_row - current_row)
    col_diff = abs(final_col - current_col)
    print(row_diff, col_diff)
    count_m = []

    for i in range(8):
        temp = []
        for j in range(8):
            temp.append(999999)
        
        count_m.append(temp)


    count_m[0][0] = 0
    count_m[0][1], count_m[1][0] = 3, 3
    count_m[0][2], count_m[2][0] = 2, 2
    count_m[1][1] = 4
    count_m[1][2], count_m[2][1] = 1, 1
    count_m[2][2] = 4

    for i in range(3, 8):
        for j in range(0, i+1):
            if j == i:
                count_m[j][i] = count_m[j-2][i-1] + 1
            else:
                if j == 0:
                    count_m[j][i] = min(count_m[j+1][i-2], count_m[j+2][i-1]) + 1
                elif j == 1:
                    count_m[j][i] = min(count_m[j-1][i-2], count_m[j+1][i-2]) + 1
                else:
                    count_m[j][i] = min(count_m[j-1][i-2], count_m[j-2][i-1]) + 1
                count_m[i][j] = count_m[j][i]
    
    # print(count_m)

    # for i in range(len(count_m)):
    #     for j in range(len(count_m)):
    #         print(count_m[i][j], end='\t')
    #     print()

    
    return count_m[row_diff][col_diff]


def solution_bfs(a, b):
    matrix = []

    count = 0
    for i in range(8):
        temp = []
        for j in range(8):
            temp.append(count)
            count += 1
        
        matrix.append(temp)

    
    q = [a]
    count = 0
    while q != []:
        count += 1
        temp = []
        flag = False
        for i in q:
            t = []
            if i % 8 >= 1 and i // 8 >= 2:
                t.append(i-16-1)
            if i % 8 >= 2 and i // 8 >= 1:
                t.append(i-8-2)
            if i % 8 >= 1 and i // 8 <= 5:
                t.append(i+16-1)
            if i % 8 >= 2 and i // 8 <= 6:
                t.append(i+8-2)
            if i % 8 <= 6 and i // 8 >= 2:
                t.append(i-16+1)
            if i % 8 <= 5 and i // 8 >= 1:
                t.append(i-8+2)
            if i % 8 <= 6 and i // 8 <= 5:
                t.append(i+16+1)
            if i % 8 <= 5 and i // 8 <= 6:
                t.append(i+8+2)
            # t = [(i-16-1), (i-16+1), (i+16-1), (i+16+1), (i-8+2), (i-8-2), (i+8-2), (i+8+2)]

            print("i: ", i, ",t: ", t)
            for j in t:
                if j == b:
                    flag = True
                    temp = []
                    break
                else:
                    if j >= 0 and j <= 63 and j not in temp:
                        temp.append(j)

            
            if flag == True:
                break
        print("Temp: ", temp)
        if flag == True:
            break
        
        q = temp

    return count



        
x = int(input())
y = int(input())
ans = solution(x, y)
ans2 = solution_bfs(x, y)
print("Ans: ", ans, ", Ans2: ", ans2)