#include <bits/stdc++.h>

using namespace std;

void deputy_chef(vector<int> a, vector<int> d, int n) {
	vector<int> survived;
	for(int i = 0; i < n; i++) {
		// cout << "I-1: " << (i-1)%n << "\n";
		// cout << "I+1: " << (i+1)%n << "\n";
		int before = (i-1) < 0 ? a[(i-1+n)%n] : a[(i-1)%n];
		int after = a[(i+1)%n];
		// cout << "Before: " << before << "\n";
		// cout << "after: " << after << "\n";
		if(before + after < d[i])
			survived.push_back(d[i]);
	}

	// cout << "Survived array: " << "\n";
	// for(int i = 0; i < survived.size(); i++) {
	// 	cout << survived[i] << " ";
	// }
	// cout << "\n";

	if(survived.size() > 0)
		cout << *max_element(survived.begin(), survived.end()) << "\n";
	else
		cout << -1 << "\n";
}


int main() {
	int t;
	cin >> t;

	while(t--) {
		int n;
		cin >> n;
		vector<int> a(n), d(n);

		for(int i = 0; i < n; i++) {
			cin >> a[i];
		}

		for(int i = 0; i < n; i++) {
			cin >> d[i];
		}

		deputy_chef(a, d, n);
		// cout << -1%4 << "\n";
	}

	return 0;
}