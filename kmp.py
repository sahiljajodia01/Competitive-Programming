# import pysnooper


# @pysnooper.snoop()
def kmp(string, pattern):
    pattern_seq = [0 for i in range(len(pattern))]
    j = 0
    i = 1
    matched_index = -1
    
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            pattern_seq[i] = j + 1
            i += 1
            j += 1
        else:
            if j != 0:
                while j != 0:
                    j = pattern_seq[j-1]
                    if pattern[j] == pattern[i]:
                        pattern_seq[i] = j + 1
                        i += 1
                        j += 1
                        break
                
                if j == 0:
                    pattern_seq[i] = 0
                    i += 1
            else:
                pattern_seq[i] = 0
                i += 1
    # print(pattern_seq)
    j = 0
    i = 0
    while i < len(string):
        if j == len(pattern):
            break
        if string[i] == pattern[j]:
            j += 1
            i += 1
        else:
            if j == 0:
                i += 1
                continue
            j = pattern_seq[j-1]

    if j == len(pattern):
        matched_index = i - len(pattern) 

    return matched_index

string1 = "abxabcabcaby"
pattern1 = "abcaby"
string = "aaabaaabbbabaa"
pattern = "babb"
ans = kmp(string, pattern)
print("My ans: ", ans)

ans1 = string.find(pattern)
print("Python builtin: ", ans1)
