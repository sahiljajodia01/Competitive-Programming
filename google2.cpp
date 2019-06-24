#include <bits/stdc++.h>

using namespace std;

int dfs(map<int, vector<int> > m, vector<int> d) {
        
}


int main() {
    int t;

    cin >> t;
    while(t--) {
        map<int, vector<int> > m1;
        int n;

        cin >> n;

        for(int i = 0; i < n; i++) {
            int x, y;

            cin >> x >> y;

            if(m1.find(x) == m1.end()) {
                m[x].push_back(y);
            }

            if(m1.find(x) == m1.end()) {
                m[y].push_back(x);
            }
        }

        for(int i = 1; i <= n; i++) {
            vector<int> temp;
            temp.push_back(i);
            int ans = dfs(m1, temp);
        }

        
        
    }

    return 0;
}