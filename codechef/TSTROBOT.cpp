#include <bits/stdc++.h>

using namespace std;

void tst_robot(int x, string s) {
    unordered_map<int, int> m;
    int count = 0;
    m[x] = 1;
    count++;
    for(int i = 0; i < s.length(); i++) {
        if(s[i] == 'L') {
            x--;
            if(m.find(x) == m.end()) {
                m[x] = 1;
                count++;
            }
        }
        else {
            x++;
            if(m.find(x) == m.end()) {
                m[x] = 1;
                count++;
            }
        }
    }

    cout << count << "\n";
}

int main() {
    int t;

    cin >> t;

    while(t--) {
        int n, x;

        cin >> n >> x;

        string s;
        cin >> s;

        tst_robot(x, s);
    }

    return 0;
}