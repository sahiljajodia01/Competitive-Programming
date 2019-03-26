#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;

    cin >> s;
    int count = 0;
    for(int i = s.length()-1; i>=0; i--) {
        // cout << "I: " << i << "\n";
        if(s[i] == '1') {
            count++;
            for(int j = 0; j < i+1; j++) {
                if(s[j] == '0') {
                    s[j] = '1';
                    // cout << "s[i]:" << s[i] << "\n";
                }
                else {
                    s[j] = '0';
                }
                // cout << s[i] << " ";
            }
            // cout << "\n";
            // cout << "String: " << s << "\n";
        }
        // cout << "String :" << s << "\n";
    }

    cout << count << "\n";
}