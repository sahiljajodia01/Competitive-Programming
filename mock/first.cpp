#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;


ll euclid(ll a, ll b)
{
	// do until the two numbers become equal
	while (a != b)
	{
		// replace larger number by its difference with the smaller number
		if (a > b)
		   a = a - b;
		else
		   b = b - a; 
	}

	return a;		// or b (since both are equal)
}


void find_common(ll ai, ll aj, ll di, ll dj) {
    ll series1 = ai, series2 = aj;
    vector<ll> vi, vj;
    // ll c = 9999;
    // while(c--) {
    //     if (series1 > series2) {
    //         series2 += dj;
    //     }
    //     else {
    //         series1 += di;
    //     }

    //     if(series1 == series2) {
    //         cout << "YES" << "\n";
    //         return;
    //     }
    // }


    // ll d = (ai - aj) + (dj - di);

    // for(ll i = 0; i < 9999; i++) {
    //     ll c = dj * i + d;

    //     if(c % di == 0) {
    //         cout << "YES" << "\n";
    //         return;
    //     }
    // }

    ll check = (ai - aj) + (dj - di);

    ll gcd = euclid(di, dj);

    if(check % gcd == 0) {
        cout << "YES" << "\n";
    }
    else {
        cout << "NO" << "\n";
    }
    // for(ll i = 0; i < 10; i++) {
    //     ll a = ai + i*di;
    //     ll b = aj + i*dj;
    //     vi.push_back(a);
    //     vj.push_back(b);


    // }

    // map<ll, ll> m;

    // for(ll i = 0; i < vi.size(); i++) {
    //     if(m.find(vi[i]) == m.end()) {
    //         m[vi[i]] = 1;
    //     }
    //     else {
    //         m[vi[i]]++;
    //     }
    // }

    // ll flag = 0;
    // for(ll i = 0; i < vj.size(); i++) {
    //     if(m.find(vj[i]) != m.end()) {
    //         cout << "YES" << "\n";
    //         return;
    //     }
    // }

    // cout << "NO" << "\n";
}

int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll ai, aj, di, dj;

        cin >> ai >> aj >> di >> dj;


        find_common(ai, aj, di, dj);
    }


    return 0;
}