#include <bits/stdc++.h>

using namespace std;

void deputy_chef(vector<int> a, vector<int> d, int n) {
	
}


int main() {
	int t;
	cin >> t;

	while(t--) {
		int n;
		vector<int> a(n), d(n);

		for(int i = 0; i < n; i++) {
			cin >> a[i];
		}

		for(int i = 0; i < n; i++) {
			cin >> d[i];
		}

		deputy_chef(a, d, n);
	}

	return 0;
}