#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
vector<ll> nb;

void nbonacci(ll n, ll v1, ll s) {

    if(v1 > n) {
        for(ll i = n; i < v1; i++) {
            ll temp = nb[i-s];
            for(ll j = i - s+1; j < i; j++) {
                temp ^= nb[j];
            }
            nb.push_back(temp);
        }
    }
    ll ans = nb[0];
    for(ll i = 1; i < v1; i++) {
        ans ^= nb[i];
    }

    cout << ans << "\n";


    // cout << "Inside nboc: " << "\n";

    // cout << "Before 1st for: " << "\n";
    // for(ll i = 0; i < v.size(); i++) {
    //     nb.push_back(v[i]);
    // }

    // cout << "Before 2nd for: " << "\n";
    // nb.push_back(v[0]);
    // for(ll i = 1; i < v.size(); i++) {
    //     nb[v.size()] ^= v[i];
    // }
    // cout << "Before last for: " << "\n";
    // for(ll i = v.size()+1; i < 1000000000; i++) {
    //     ll temp = nb[i-1]^nb[i-v.size()]^nb[i-1];
    //     nb.push_back(temp);
    // }

    // cout << "Before output: " << "\n";
    // cout << nb[(v1 - 1)] << "\n";
}



int main() {
    ll n, q;


    cin >> n >> q;

    
    vector<ll> v(n);
    // vector<ll> v1(q);

    for(ll i = 0; i < n; i++) {
        ll temp;
        cin >> temp;
        v[i] = temp;
        nb.push_back(temp);
    }

    for(ll i = 0; i < q; i++) {
        cout << "Inside :" << "\n";
        ll temp;
        cin >> temp;
        nbonacci(nb.size(), temp, v.size());
    }


    return 0;
}