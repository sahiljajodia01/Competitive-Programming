// Seems easy but is actually hard. Wrong answer

#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
    ll t;
    cin >> t;

    while(t--) {
        ll l, r, g;

        cin >> l >> r >> g;
        ll count = 0;
        for(ll i = l; i <= r; i++) {
            if(i % g == 0) {
                count++;
            }
        }

        cout << count << "\n";
    }

    return 0;
}