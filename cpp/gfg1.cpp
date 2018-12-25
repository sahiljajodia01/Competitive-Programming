#include <bits/stdc++.h>

using namespace std;

bool palindrome(string s) {
    int low = 0;
    int high = s.length() - 1;

    while(high > low) {
        if(s[low++] != s[high--]) {
            return false;
        }

    }
    return true;
}

void allPossiblePalindrome(string s, int start) {
    // vector<string> allPalindromes;
    // string::iterator it;
    int i, j;
    int length = s.length();
    string temp;
    int count = 0;
    if(start >= s.length()) {
        return;
    }
    else {
        for(i = start; i < s.length(); i++) {
            temp = s.substr(start, count + 1);
            // cout << "Temp is: " << temp << "\n";
            if(palindrome(temp)) {
                cout << temp << "\n";
            }
            count++;
        }
    }
    return allPossiblePalindrome(s, start + 1);
}

int main() {
    cout << "Enter a string: ";
    string s;
    cin >> s;
    int len = s.length();

    allPossiblePalindrome(s, 0);


    return 0;
}