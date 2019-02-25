t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    d = {}
    for i in range(len(s)):
        sub = s[0:i+1]
        d[sub] = 1

    count = 0
    final_key = ""
    # print(len(final_key))
    for key in d:
        temp = s.count(key)

        # print("Temp: ", temp)
        # print("Key len", len(key))
        if temp >= count and len(key) > len(final_key):
            count = temp
            final_key = key

        # print("Count: ", count)
        # print("Final key: ", final_key)

    print(final_key)
