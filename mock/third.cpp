#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

void find_pairs(vector< pair<ll, ll> > v, ll s) {
    ll count = v.size();
    for(ll i = 0; i < v.size(); i++) {
        for(ll j = i+1; j < v.size(); j++) {
            ll cal = (v[i].first - v[j].first) + (v[i].second - v[j].second);
            cout << "i: " << i << " j: " << j << " Cal: " << cal << "\n";

            if((v[i].first > 0 && v[j].first < 0) || (v[j].first > 0 && v[i].first < 0) || ((v[i].second > 0 && v[j].second < 0)) || (v[j].second > 0 && v[i].second < 0)) {
                if(cal == s) {
                 count += 1;
                }
            }
            else {
                if(cal == s) {
                 count += 2;
                }
            }
            
        }
    }

    cout << count << "\n";
}

int main() {
    ll n, s;
    cin >> n;
    vector< pair<ll, ll> > v;
    while(n--) {
        ll a, b;
        cin >> a >> b;
        v.push_back(make_pair(a, b));
    }

    cin >> s;


    find_pairs(v, s);


}