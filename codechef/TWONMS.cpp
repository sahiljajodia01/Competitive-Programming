#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll a, b, n;

        cin >> a >> b >> n;

        ll bob_turns = n/2;
        ll alice_turns = n - n/2;
        // if(n%2 == 0)
        //     alice_turns = n/2;
        // else
        //     alice_turns = n/2 + 1;


        a = a * pow(2, alice_turns);
        b = b * pow(2, bob_turns);
        // for(ll i = 0; i < n; i++) {
        //     if(i%2 == 0) {
        //         a *= 2;
        //     }
        //     else {
        //         b *= 2;
        //     }
        // }

        ll max = a > b ? a : b;
        ll min = a < b ? a : b;
        ll ans = max/min;
        cout << ans << "\n";
    }

    return 0;
}