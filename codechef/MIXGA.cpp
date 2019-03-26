#include <bits/stdc++.h>

using namespace std;

void mixga(vector<int> v, int k) {
    int ans = 0;
    for(int i = 0; i < v.size(); i++) {
        if(i % 2 != 0) {
            if (ans > 0) {
                ans -= v[i];
            }
            else if(ans < 0) {
                ans += v[i];
            }
            else {
                ans += v[i];
            }
        }
        else {
            if (ans < 0) {
                ans -= v[i];
            }
            else if(ans > 0) {
                ans += v[i];
            }
            else {
                ans += v[i];
            }
        }
    }
    ans = abs(ans);
    if(ans >= k) {
        cout << 1 << "\n";
    }
    else {
        cout << 2 << "\n";
    }
}


int main() {
    int t;

    cin >> t;

    while(t--) {
        int n, k;

        cin >> n >> k;

        vector<int> v(n);

        for(int i = 0; i < n; i++) {
            cin >> v[i];
        }

        mixga(v, k);
    }

    return 0;
}