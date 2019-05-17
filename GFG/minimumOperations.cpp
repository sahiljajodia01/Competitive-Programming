#include <bits/stdc++.h>

using namespace std;

int a[10001] = {};

int minimum_operations(int n) {
    if(n == 1) {
        return 1;
    }

    if(a[n] != 0) {
        return a[n];
    }
    else {
        if(n % 2 == 0) {
            a[n] = 1 + minimum_operations(n/2);
            return a[n];
        }
        else {
            a[n] = 2 + minimum_operations(n/2);
            return a[n];
        }
    }
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        int ans = minimum_operations(n);

        cout << ans << "\n";
    }

    return 0;
}