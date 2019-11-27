# import pysnooper


# @pysnooper.snoop()
def kmp(string, pattern):
    matched_index = -1
    

    # First Finding the pattern sequence
    # Here it checks if there is a suffix which is equal to prefix before the current mismatched character
    # Initially j = 0 and i = 1
    j = 0
    i = 1
    # Initializing the pattern sequence by zeroes
    pattern_seq = [0 for i in range(len(pattern))]
    # Calculating pattern sequence array. Time complexity is O[len(pattern)]
    while i < len(pattern):
        # If ith and jth character is same then seq = j+1
        if pattern[i] == pattern[j]:
            pattern_seq[i] = j + 1
            i += 1
            j += 1
        else:
            # Bring the j back to the pattern seq value of current j-1
            # Then again check if jth and ith character is same
            # If not then continue this process until j is not 0
            # If j is 0 and jth and ith character does not match then put pattern seq as 0 and increment i
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


    # Then after calculating the pattern sequence array, now we will use it for string matching
    j = 0
    i = 0
    while i < len(string):
        # If length of j is equal to pattern, then pattern is matched so break out of loop
        if j == len(pattern):
            break

        # If pattern matches then increment i and j
        if string[i] == pattern[j]:
            j += 1
            i += 1
        else:
        # if pattern does not match, then check from which pattern character we can continue processing
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
