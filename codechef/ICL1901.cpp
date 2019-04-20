#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;


int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll n, k;
        cin >> n >> k;

        ll copy = n;

        map<ll, ll> m;
        // ll flag = 0;
        while(copy != 0) {
            ll temp = copy % 10;

            if(m.find(temp) == m.end()) {
                m[temp] = 1;
            }

            copy /= 10;
        }

        ll si = m.size();

        // cout << "Size: " << si << "\n";

        if(si == 1) {
            cout << 1 << "\n";
        }
        else if(si == 2) {
            cout << 8 << "\n";
        }
        else {
            cout << 27 << "\n";
        }
    }

    return 0;
}