#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

ll diff_days(string s, string e) {
    ll diff = 0;
    // if(s == "monday") {
    //     if(e == "monday") {
    //         diff = 1;
    //     }
    //     if(e == "tuesday") {
    //         diff = 2;
    //     }
    //     if(e == "wednesday") {
    //         diff = 3;
    //     }
    //     if(e == "thursday") {
    //         diff = 4;
    //     }
    //     if(e == "friday") {
    //         diff = 5;
    //     }
    //     if(e == "saturday") {
    //         diff = 6;
    //     }
    //     if(e == "sunday") {
    //         diff = 7;
    //     }
    // }
    // else if(s == "tuesday") {
    //     if(e == "monday") {
    //         diff = 7;
    //     }
    //     if(e == "tuesday") {
    //         diff = 1;
    //     }
    //     if(e == "wednesday") {
    //         diff = 2;
    //     }
    //     if(e == "thursday") {
    //         diff = 3;
    //     }
    //     if(e == "friday") {
    //         diff = 4;
    //     }
    //     if(e == "saturday") {
    //         diff = 5;
    //     }
    //     if(e == "sunday") {
    //         diff = 6;
    //     }
    // }
    // else if(s == "wednesday") {
    //     if(e == "monday") {
    //         diff = 6;
    //     }
    //     if(e == "tuesday") {
    //         diff = 7;
    //     }
    //     if(e == "wednesday") {
    //         diff = 1;
    //     }
    //     if(e == "thursday") {
    //         diff = 2;
    //     }
    //     if(e == "friday") {
    //         diff = 3;
    //     }
    //     if(e == "saturday") {
    //         diff = 4;
    //     }
    //     if(e == "sunday") {
    //         diff = 5;
    //     }
    // }
    // else if(s == "thursday") {
    //     if(e == "monday") {
    //         diff = 5;
    //     }
    //     if(e == "tuesday") {
    //         diff = 6;
    //     }
    //     if(e == "wednesday") {
    //         diff = 7;
    //     }
    //     if(e == "thursday") {
    //         diff = 1;
    //     }
    //     if(e == "friday") {
    //         diff = 2;
    //     }
    //     if(e == "saturday") {
    //         diff = 3;
    //     }
    //     if(e == "sunday") {
    //         diff = 4;
    //     }
    // }
    // else if(s == "friday") {
    //     if(e == "monday") {
    //         diff = 4;
    //     }
    //     if(e == "tuesday") {
    //         diff = 5;
    //     }
    //     if(e == "wednesday") {
    //         diff = 6;
    //     }
    //     if(e == "thursday") {
    //         diff = 7;
    //     }
    //     if(e == "friday") {
    //         diff = 1;
    //     }
    //     if(e == "saturday") {
    //         diff = 2;
    //     }
    //     if(e == "sunday") {
    //         diff = 3;
    //     }
    // }
    // else if(s == "saturday") {
    //     if(e == "monday") {
    //         diff = 3;
    //     }
    //     if(e == "tuesday") {
    //         diff = 4;
    //     }
    //     if(e == "wednesday") {
    //         diff = 5;
    //     }
    //     if(e == "thursday") {
    //         diff = 6;
    //     }
    //     if(e == "friday") {
    //         diff = 7;
    //     }
    //     if(e == "saturday") {
    //         diff = 1;
    //     }
    //     if(e == "sunday") {
    //         diff = 2;
    //     }
    // }
    // else if(s == "sunday") {
    //     if(e == "monday") {
    //         diff = 2;
    //     }
    //     if(e == "tuesday") {
    //         diff = 3;
    //     }
    //     if(e == "wednesday") {
    //         diff = 4;
    //     }
    //     if(e == "thursday") {
    //         diff = 5;
    //     }
    //     if(e == "friday") {
    //         diff = 6;
    //     }
    //     if(e == "saturday") {
    //         diff = 7;
    //     }
    //     if(e == "sunday") {
    //         diff = 1;
    //     }
    // }


    map<string,ll> days;
    days["monday"]=1;
    days["tuesday"]=2;
    days["wednesday"]=3;
    days["thursday"]=4;
    days["friday"]=5;
    days["saturday"]=6;
    days["sunday"]=7;


    if(days.at(s)<days.at(e))
        diff=days.at(e)-days.at(s)+1;
    else if(days.at(e)<days.at(s))
        diff=7-(days.at(s)-days.at(e))+1;
    else
        diff=1;

    return diff;
}


void event(string s, string e, ll l, ll r) {
    // if(r - l <= 7) {
    //     ll diff = diff_days(s, e);
    //     if(diff < l) {
    //         cout << "impossible" << "\n";
    //     }
    //     else {
    //         cout << diff << "\n";
    //     }
    // }
    // else {
    //     ll diff = diff_days(s, e);

    //     if(diff < l ) {
    //         cout << "impossible" << "\n";
    //     }
    //     else {
    //         cout << "many" << "\n";
    //     }
    // }
    ll diff = diff_days(s, e);
    // cout << "Diff: " << diff << "\n";
    ll count = 0, i = 0, sum, ans;
    // cout << "Diff: " << diff << "\n";
    
        while(sum <= r) {
            sum = diff + 7*i;
            if(sum >= l && sum <= r) {
                count++;
                ans = sum;
            }
            i++;
        }

    if(count == 1) {
        cout << diff << "\n";
    }
    else if(count > 1) {
        cout << "many" << "\n";
    }
    else {
        cout << "impossible" << "\n";
    }
        // if(diff + 7 > r) {
        //     cout << diff << "\n";
        // }
        // else {
        //     cout << "many" << "\n";
        // }
}

int main() {
    ll t;

    cin >> t;

    while(t--) {
        string s, e;
        ll l, r;

        cin >> s >> e >> l >> r;

        event(s, e, l, r);

    }


    return 0;
}