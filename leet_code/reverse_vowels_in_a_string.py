
# Google

def reverseVowels(s: str) -> str:
    s = list(s)

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_list = []
    for i in range(len(s)):
        if s[i] in vowels:
            vowels_list.append(s[i])
            
    
    vowels_list = vowels_list[::-1]

    counter = 0
    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = vowels_list[counter]
            counter += 1
            
    s = ''.join(s)
    
    return s