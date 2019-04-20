#include <bits/stdc++.h>

using namespace std;

void friends_or_girlfriend(string s, char c) {
    vector<int> v;

    for(int i = 0; i < s.length(); i++) {
        if(s[i] == c)
            v.push_back(i);
    }

    // cout << "Index vector: " << "\n";
    // for(int i = 0; i < v.size(); i++) {
    //     cout << v[i] << " ";
    // }
    // cout << "\n";

    
    int count = 0;
    for(int i = 0; i < v.size(); i++) {
        if((i != 0) && (i != v.size() - 1)) {
            // cout << "First if" << "\n";
            // cout << "Before s1" << "\n";
            int s1 = v[i] - v[i-1] - 1;
            // cout << "Between" << "\n";
            int s2 = v[i+1] - v[i] - 1;
            // cout << "After s2" << "\n";

            count += v[i-1] + 1;

            count += s1*s2;
            count++;
            count += s1 + s2;

            // cout << "s1: " << s1 << "\n";
            // cout << "s2: " << s2 << "\n";
        }
        else if(i == 0) {
            // cout << "Second if" << "\n";
            // cout << "Before s1" << "\n";
            int s1 = v[i] - 0;
            // cout << "Between" << "\n";
            int s2 = v[i+1] - v[i] - 1;
            // cout << "After s2" << "\n";

            // count += v[i] + 1;

            count += s1*s2;
            count++;
            count += s1 + s2;

            // cout << "s1: " << s1 << "\n";
            // cout << "s2: " << s2 << "\n";
            // cout << "Count: " << count << "\n";
        }
        else if(i == v.size() - 1) {
            // cout << "Third if" << "\n";
            // cout << "Before s1" << "\n";
            int s1 = v[i] - v[i-1] - 1;
            // cout << "Between" << "\n";
            int s2 = s.length() - 1 - v[i];
            // cout << "After s2" << "\n";

            count += v[i-1] + 1;

            count += s1*s2;
            count++;
            count += s1 + s2;

            // cout << "s1: " << s1 << "\n";
            // cout << "s2: " << s2 << "\n";
            // cout << "Count: " << count << "\n";
        }
        
    }

    cout << count << "\n";
}

int main() {
    int t;

    cin >> t;

    while(t--) {
        int n;
        cin >> n;
        string s;
        char c;

        cin >> s;
        cin >> c;

        friends_or_girlfriend(s, c);
    }


    return 0;
}