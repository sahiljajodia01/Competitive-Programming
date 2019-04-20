#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll n, m, k;


        cin >> n >> m >> k;
        ll a = 0;


        // for(ll i = n; i >= m; i--) {
        //     if(i%m == 0) {
        //         a = i;
        //         break;
        //     }
        // }
        a = n/m;

        ll diff = n - m*a;

        // cout << "Diff: " <<diff << "\n";
        if(m > n) {
            // if(n % k == 0)
            //     cout << n/k << "\n";
            // else
            //     cout << -1 << "\n";
            cout << -1 << "\n";
        }
        else if(m == n) {
            cout << 0 << "\n";
        }
        else if(k > diff) {
            cout << -1 << "\n";
        }
        else {
            // cout << "Inside else" << "\n";
            ll ans;

            if(diff % k == 0) {
                ans = diff/k;
            }
            else {
                ans = -1;
            }
            cout << ans << "\n";
        }


    }

    return 0;
}