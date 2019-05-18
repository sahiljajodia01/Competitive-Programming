#include <bits/stdc++.h>

using namespace std;

int a[100001] = {};

int maximum_sum(int n) {
    // int sum = 0;
    if(n == 0)
        return 0;
    else if(n == 1)
        return 1; 

    if(a[n] != 0) {
        return a[n];
    }
    else {
        int sum = maximum_sum(n/2) + maximum_sum(n/3) + maximum_sum(n/4);
        if(sum > n) {
            a[n] = sum;
            return a[n];
        }
        else {
            a[n] = n;
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
        int max = n;
        int ans = maximum_sum(n);

        cout << ans << "\n";
    }

    return 0;
}