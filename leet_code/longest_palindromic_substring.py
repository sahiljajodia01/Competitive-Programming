# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/


######### Recursive solution. Time limit exceeded #########
def longestPalindrome(s: str) -> str:
    def solve(s, start, end):
        if start > end:
            return ""
        string = s[start:(end+1)]
        if string == string[::-1]:
            return string
        
        left = solve(s, start+1, end)
        right = solve(s, start, end-1)
        
        if left == "" and right != "":
            return right
        elif left != "" and right == "":
            return left
        elif left == "" and right == "":
            return ""
        else:
            if len(left) > len(right):
                return left
            else:
                return right
        
    return solve(s, 0, len(s)-1)


######## Expand from center solution. Time[O(n^2)] and Space[O(1)] #########
def longestPalindrome(s: str) -> str:
    def solve(s, left, right):
        longest_substring = ""
        while left >= 0 and right <= len(s) - 1:
            string = s[left:(right+1)]
            if string == string[::-1]:
                if len(string) > len(longest_substring):
                    longest_substring = string
            
            left -= 1
            right += 1
        
        return longest_substring
    
    longest = ""
    for i in range(len(s)):
        string1 = solve(s, i, i)
        string2 = solve(s, i, i+1)
        
        if len(string1) > len(string2):
            max_string = string1
        else:
            max_string = string2
        
        
        if len(max_string) > len(longest):
            longest = max_string
    
    return longest


palin = longestPalindrome("babaddtattarrattatddetartrateedredividerb")
print(palin)
