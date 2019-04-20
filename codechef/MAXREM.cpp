#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
    ll n;

    cin >> n;
    vector<ll> v(n);
    for(ll i = 0; i < n; i++) {
        cin >> v[i];
    }

    ll largest = v[0];
    ll sec_largest = v[0];



    for(ll i = 0; i < n; i++) {
        if(largest < v[i]) {
            largest = v[i];
        }
    }

    for(int i = 0; i < n; i++) {
        if(sec_largest < v[i] && v[i] < largest) {
            sec_largest = v[i];
        }
    }
    cout << sec_largest % largest << "\n";
    // ll max = 0;

    // for(ll i = 0; i < n; i++) {
    //     if(largest % v[i] > max) {
    //         max = largest % v[i];
    //     }
    // }

    // ll final_ans = sec_largest > max ? sec_largest : max;

    // cout << sec_largest << "\n";

    return 0;
}