#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;

void prob_number(vector<ll> v, vector<ll> p, vector<ll> q) {
    ll min_k = LONG_MAX;
    ll max_k = 0;
    vector<ll> index;

    ll max = *max_element(v.begin(), v.end());
    ll min = *min_element(v.begin(), v.end());

    // cout << "Max: " << max << "\n";
    // cout << "Min: " << min << "\n";
    for(ll i = 0; i < v.size(); i++) {
        if(v[i] == max) {
            index.push_back(i);
        }
    }

    
    for(ll i = 0; i < index.size(); i++) {
        if(v[index[i]] - q[index[i]] < min_k) {
            min_k = v[index[i]] - q[index[i]];
        }
    }
    index.clear();
    for(ll i = 0; i < v.size(); i++) {
        if(v[i] == min) {
            index.push_back(i);
        }
    }

    
    for(ll i = 0; i < index.size(); i++) {
        if(v[index[i]] + p[index[i]] > max_k) {
            max_k = v[index[i]] + p[index[i]];
        }
    }

    // cout << "Min k: " << min_k << "\n";
    // cout << "MAx_k: " << max_k << "\n";

    if(min_k > max_k) {
        cout << 0 << "\n";
        return;
    }
    ll count = 0;
    for(ll i = min_k; i <= max_k; i++) {
        int flag = 0;
        for(ll j = 0; j < v.size(); j++) {

            if(i >= v[j]) {
                if(abs(v[j] - i) <= p[j])
                    continue;
                else {
                    flag = 1;
                    break;
                }
            }
            else {
                if(abs(v[j] - i) <= q[j])
                    continue;
                else {
                    flag = 1;
                    break;
                }
            }
            // if(abs(v[j] - i) <= p[j] || abs(v[j] - i) <= q[j]) {
            //     continue;
            // }
            // else {
            //     flag = 1;
            //     break;
            // }
        }

        if(flag == 0) {
            // cout << "K: " << i << "\n";
            count++;
        }
        
    }


    cout << count << "\n";


    // for(int i = 0; i < v.size(); i++) {
    //     if(v[i] - q[i] < min_k) {
    //         min = v[i] - q[i];
    //     }
        
    //     if(v[i] + p[i] > max_k) {
    //         max_k = v[i] + p[i];
    //     }
    // }
}

int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll n;
        cin >> n;

        vector<ll> v(n), p(n), q(n);

        for(ll i = 0; i < n; i++) {
            cin >> v[i];
        }

        for(ll i = 0; i < n; i++) {
            cin >> p[i];
        }

        for(ll i = 0; i < n; i++) {
            cin >> q[i];
        }
        prob_number(v, p, q);
    }
    return 0;
    
}