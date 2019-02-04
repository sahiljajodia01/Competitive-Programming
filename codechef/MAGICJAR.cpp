#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

void magic_jar(vector<ll> v) {
	ll total = 0;

	for(ll i = 0; i < v.size(); i++) {
		total += v[i] - 1;
	}
	total += 1;

	cout << total << "\n";
}

int main() {
	int t;

	cin >> t;

	while(t--) {
		ll n;
		cin >> n;
		vector<ll> v(n);

		for(ll i = 0; i < n; i++) {
			cin >> v[i];
		}

		magic_jar(v);
	}

	return 0;
}