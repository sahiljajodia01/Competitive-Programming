n = int(input())

ins = input()

string = ""

for i in ins:
    if i == "1":
        string += "a"
    elif i == "2":
        string += "bb"
    elif i == "3":
        string += "ab"
    else:
        arr = string.split()

        for i in range(len(arr)):
            if arr[i] == 'a':
                arr[i] = 'b'
            elif arr[i] == 'b':
                arr[i] = 'a'


print(string)