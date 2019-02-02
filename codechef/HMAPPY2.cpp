#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

ll gcd(ll a, ll b) {
		
	if (b == 0)
		return a;

	return gcd(b, a%b);


}

void contest(ll n, ll a, ll b, ll k) {
	ll lcm = (a*b)/gcd(a, b);

	ll ans = n/a + n/b - 2*(n/lcm);

	if(ans >= k)
		cout << "Win" << "\n";
	else
		cout << "Lose" << "\n";
}

// inline void scanint(int &x) {
//     register int c = getchar_unlocked();
//     x = 0;
//     int neg = 0;
 
//     for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());
 
//     if(c=='-') {
//         neg = 1;
//         c = getchar_unlocked();
//     }
 
//     for(; c>47 && c<58 ; c = getchar_unlocked()) {
//         x = (x<<1) + (x<<3) + c - 48;
//     }
 
//     if(neg)
//         x = -x;
// }


int main() {
	int t;

	cin >> t;

	while(t--) {
		ll n, a, b, k;

		cin >> n >> a >> b >> k;

		contest(n, a, b, k);
	}

	return 0;
}