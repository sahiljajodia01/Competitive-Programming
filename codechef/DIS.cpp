#include <bits/stdc++.h>

using namespace std;

void distance(int n, vector<float> a, vector<float> b) {
	if(b[0] != a[n-1] || b[n-1] != a[0]) {
		// cout << "Executed 1st if" << "\n";s
		cout << "No" << "\n";
		return;
	}
	int flag = 0;
	for(int i = 1; i < n-1; i++) {
		// float sum = 0;
		// for(int i = 1; i < n - i)
		if(b[i] < (a[n-1] - a[n-i-1])) {
			// cout << "Executed 2nd if inside for" << "\n";
			flag = 1;
			break;
		}
	}
	if(flag == 1) {
		cout << "No" << "\n";
	}
	else {
		cout << "Yes" << "\n";
	}
}

int main() {
	int t;

	cin >> t;

	while(t--) {
		int n;
		cin >> n;

		vector<float> a, b;

		for(int i = 0; i < n; i++) {
			float temp;
			cin >> temp;

			a.push_back(temp);
		}

		for(int i = 0; i < n; i++) {
			float temp;
			cin >> temp;

			b.push_back(temp);
		}

		distance(n, a, b);
	}

	return 0;
}