# import pysnooper

# @pysnooper.snoop()
def longestCommonPrefix(A):
    counter = 0
    string = []
    for _ in range(len(A[0])):
        char = A[0][counter]
        flag = 0
        for i in range(1, len(A)):
            if _ >= len(A[i]):
                flag = 1
                break
            else:
                if A[i][counter] == char:
                    continue
                else:
                    flag = 1
                    break

        if flag == 0:
            string.append(char)
        counter += 1

    string = ''.join(string)

    print("String: ", string)


longestCommonPrefix(["abcdefgh", "abcefgh", "aefghijk"])
longestCommonPrefix(["abab", "ab", "abcd"])
        