#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;

    cin >> t;

    while(t--) {
        string s;
        cin >> s;
        vector<char> v;
        for(int i = 0; i < s.length(); i++) {
            if(isalpha(s[i])) {
                v.push_back(s[i]);
            }
        }


        int counter = v.size() - 1;

        for(int i = 0; i < s.length(); i++) {
            if(isalpha(s[i])) {
                s[i] = v[counter];
                counter--;
            }
        }

        cout << "Reverse string: " << s << "\n";
    }

    return 0;
}