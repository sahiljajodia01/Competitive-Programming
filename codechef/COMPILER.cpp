#include <bits/stdc++.h>

using namespace std;


void compiler(string s) {
    stack<char> st;
    int count = 0;
    // int flag = 0;
    int temp = 0;
    for(int i = 0; i < s.length(); i++) {
        if(st.empty()) {
            if(s[i] == '>') {
                count += temp;
                temp = 0;
                break;
            }
            else {
                count += temp;
                temp = 0;
                st.push('<');
                temp++;
            }
        }
        else {
            if(s[i] == '>') {
                st.pop();
                temp++;
            }
            else {
                st.push('<');
                temp++;
            }
        }
    }
    if(st.empty()) {
        count += temp;
    }
    // count += temp;
    
    cout << count << "\n";
    
}


int main() {
    int t;
    cin >> t;

    while(t--) {
        string s;

        cin >> s;

        compiler(s);
    }

    return 0;
}