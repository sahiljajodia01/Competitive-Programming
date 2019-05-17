#include <bits/stdc++.h>

using namespace std;

const unsigned int M = 1000000007;

typedef long long ll;

vector<ll> dp(1000001, 0);

// ll fact(ll aa) {

// 	if (aa == 0 || aa == 1) {
// 		return 1;
// 	} else {
// 		if (dp[aa] != 0)
// 			return dp[aa];
// 		else
// 			dp[aa] = (aa * fact(aa - 1));
//             dp[aa] = dp[aa] % M;
//             return dp[aa];
// 	}

// }

ll fact(ll n) {
    // ll result = 1;
    dp[1] = 1;
    if(dp[n] != 0) {
        return dp[n];
    }
    for(ll i = 2; i <= n; i++) {
        dp[i] = dp[i-1] * i;
        dp[i] = dp[i] % M;
    }
    return dp[n];
}


int main() {
    ll t;

    cin >> t;
    vector<ll> v;
    while(t--) {
        ll n;
        cin >> n;

        ll f = fact(n+1);
        // f = f % M;
        cout << f-1 << "\n";

        // for(ll i = 1; i <= n; i++) {
        //     v.push_back(i);
        // }

        // for(ll i = 0; i < v.size(); i+= 2) {
        //     if(i == v.size() - 1) {
        //         cout << v[i] << "\n";
        //         break;
        //     }
        //     else {
        //         ll t1 = v[i];
        //         ll t2 = v[i+1];

        //         ll f = t1 + t2 + t1*t2;

        //         v.push_back(f);
        //     }
        // }
    }

    return 0;
}