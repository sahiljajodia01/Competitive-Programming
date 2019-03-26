t = int(input())

for i in range(t):
    s = input()
    # max_n = 0
    # max_s = "z"
    # dict_n = {}
    # for i in range(len(s)):
    #     for j in range(i+1, len(s)+1):
    #         sub = s[i:j]
    #         if sub in dict_n:
    #             continue
    #         else:
    #             dict_n[sub] = 1
            
    #         c = s.count(sub)
    #         print("sub: ", sub, " Count: ", c)

    #         if c >= max_n and sub < max_s:
    #             max_n = c
    #             max_s = sub

    
    # print(max_s)

    dict_n = {}
    for i in range(len(s)):
        if s[i] in dict_n:
            dict_n[s[i]] = dict_n[s[i]] + 1
        else:
            dict_n[s[i]] = 1

    # print(dict_n)

    max_n = 0
    sub_n = 'z'
    strings = []
    for key, val in dict_n.items():
        if val > max_n:
            max_n = val


    for key, val in dict_n.items():
        if val == max_n:
            strings.append(key)

    sub_n = sorted(strings)[0]

    print(sub_n)
