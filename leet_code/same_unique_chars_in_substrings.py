import random

def solution(s):

    d = {}

    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1

    t = {}
    count = 0
    for i in range(len(s)):
        # a = s[:i+1]
        # b = s[i+1:]

        char = s[i]

        d[s[i]] -= 1

        if d[s[i]] == 0:
            del d[s[i]]
        
        if char in t.keys():
            t[char] += 1
        else:
            t[char] = 1
        
        if len(t) == len(d):
            count += 1

    return count


strings = ["aabca", "aabc", "abcacba", "".join([random.choice(["a", "b", "c", "d"]) for i in range(200000)])]
for i in strings:
    ans = solution(i)
    print(ans)
