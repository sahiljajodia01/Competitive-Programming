#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

void trick(ll a) {
    ll d1, d2;

    ll count = 0;
    ll sum_chef = 0, sum_friend = 0;
    ll total_money = 0;
    while(true) {
        // cout << "HEl" << "\n";
        ll chef_money = pow(2, count);

        ll friend_money = a;
        // cout << "Chef money: " << chef_money << "\n"; 
        sum_chef += chef_money;
        sum_friend += friend_money;

        // cout << "Chef sum: " << sum_chef << '\n';
        // cout << "Friend sum: " << sum_friend << "\n";

        ll diff = sum_friend - sum_chef;
        // cout << "Diff: " << diff << "\n";
        if(diff <= 0) {
            break;
        }
        d1 = count + 1;

        if(diff > total_money) {
            total_money = diff;
            d2 = count + 1;
        }

        count++;
    }

    cout << d1 << " " << d2 << "\n";
}

int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll a;

        cin >> a;

        trick(a);
    }
    
    return 0;
}