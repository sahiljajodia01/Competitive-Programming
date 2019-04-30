#include <bits/stdc++.h>

using namespace std;

void attendance(vector< pair<string, string> > v) {
    map<string, int> m;

    for(int i = 0; i < v.size(); i++) {
        if(m.find(v[i].first) == m.end()) {
            m[v[i].first] = 1;
        }
        else {
            m[v[i].first] += 1;
        }
    }
    
    // cout << "Map: " << "\n";
    // for(map<string, int>::iterator it = m.begin(); it != m.end(); it++) {
    //     cout << it->first << " - " << it->second << "\n";
    // }

    for(int i = 0; i < v.size(); i++) {
        if(m[v[i].first] > 1) {
            cout << v[i].first << " " << v[i].second << "\n";
        }
        else {
            cout << v[i].first << "\n";
        }
    }
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;

        cin >> n;

        vector< pair<string, string> > v;


        for (int i = 0; i < n; i++) {
            string s1, s2;

            cin >> s1 >> s2;

            v.push_back( make_pair(s1, s2) );
        }

        attendance(v);
    }

    return 0;
}