#include <bits/stdc++.h>

using namespace std;

int a[26][26] = {};

int path_to_origin(int n, int m) {
    if(n == 0 || m == 0) {
        return 1;
    }
    if(a[m][n] != 0) {
        return a[m][n];
    }
    a[m][n] = path_to_origin(n-1, m) + path_to_origin(n, m-1);
    return a[m][n];
}



int main() {
    int t;
    cin >> t;

    while(t--) {
        int n, m;

        cin >> n >> m;

        int ans = path_to_origin(n, m);

        cout << ans << "\n";
    }
}