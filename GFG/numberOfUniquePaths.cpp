#include <bits/stdc++.h>

using namespace std;

int a[100][100] = {};

int unique_paths(int m, int n) {
    if(m == 1 || n == 1) {
        return 1;
    }
    if(a[m][n] != 0) {
        return a[m][n];
    }
    else {
        a[m][n] = unique_paths(m, n-1) + unique_paths(m-1, n);
        return a[m][n];
    }
    
}

int main() {

    int t;

    cin >> t;

    while(t--) {
        int m, n;

        cin >> m >> n;

        int ans = unique_paths(m, n);

        cout << ans << "\n";
    }

    return 0;
}