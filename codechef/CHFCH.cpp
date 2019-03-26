#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

void chef_chal(vector<ll> v, ll k) {
    map<ll, ll> m;
    ll min_swaps = LONG_MAX;

    for(ll i = 0; i < v.size(); i++) {
        if(m.find(v[i]) == m.end()) {
            m[v[i]] = 1;
        }
        else {
            m[v[i]]++;
        }
    }
    ll flag = 0;
    for(map<ll, ll>::iterator it = m.begin(); it != m.end(); it++) {
        ll first = it->first;
        ll second = it->second;
         

        if(second < k) {
            continue;
        }
        flag = 1;
        // cout << "For first = " << first << "\n";
        vector<ll> ind;
        for(ll i = 0; i < v.size(); i++) {
            if(v[i] == first) {
                ind.push_back(i);
            }
        }

        // cout << "Index array: " << "\n";
        // for(ll i = 0; i < ind.size(); i++) {
        //     cout << ind[i] << " ";
        // }
        // cout << "\n";
        ll dev = LONG_MAX;
        ll index = 0;
        
        for(ll i = 0; i < ind.size(); i++) {
            ll temp = 0;
            vector<ll> pre_diff;
            for(ll j = 0; j < ind.size(); j++) {
                if(i != j) {
                    // ll pr_diff = ind[j] - ind[i];
                    // pre_diff.push_back(pr_diff);
                    temp += abs(ind[j] - ind[i]);
                }
            }

            // sort(pre_diff.begin(), pre_diff.end());

            // for(ll j = 0; j < k-1; j++) {
            //     temp += pre_diff[j];
            // }

            if(temp < dev) {
                dev = temp;
                // index_of_arr = ind[i];
                index = i;
            }
        }

        // cout << "Perfect index: " << index << "\n";
        // cout << "Perfect index std: " << dev << "\n";

        ll total_swap = 0;
        vector<ll> differences;
        for(ll i = 0; i < ind.size(); i++) {
            if(index != i) {
                ll differ = abs(ind[i] - ind[index]) - abs(index - i);
                differences.push_back(differ);
                // cout << abs(ind[i] - ind[index]) - (index - i) << "\n";
                // total_swap += abs(ind[i] - ind[index]) - abs(index - i);
            }
        }

        sort(differences.begin(), differences.end());

        // cout << "Differences array: " << "\n";
        // for(int i = 0; i < differences.size(); i++) {
        //     cout << differences[i] << " ";
        // }
        // cout << "\n";

        for(ll i = 0; i < k-1; i++) {
            total_swap += differences[i];
        }

        if(total_swap < min_swaps) {
            min_swaps = total_swap;
        }

        // cout << "Total_ swaps: " << total_swap << "\n";
        // cout << "--------------------------------------------------- " << "\n";

    }
    if(flag == 0) {
        cout << -1 << "\n";
    }
    else {
        cout << min_swaps << "\n";
    }
}


int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll n, k;

        cin >> n >> k;

        vector<ll> v(n);

        for(ll i = 0; i < n; i++) {
            cin >> v[i];
        }

        chef_chal(v, k);
    }

    return 0;
}