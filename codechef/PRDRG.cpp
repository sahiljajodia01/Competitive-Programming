#include <bits/stdc++.h>

using namespace std;

vector<int> v;

void dist(int n) {
	if(n == 1) {
		v.push_back(1);
		v.push_back(2);
		return;
	}
	int num = 1, den = 2;

	for(int i = 1; i < n; i++) {
		if(i % 2 != 0) {
			num = 2*num - 1;
		}
		else {
			num = 2*num + 1;
		}
		den = 2*den;
	}
	v.push_back(num);
	v.push_back(den);
	return;
}


int main() {
	int t;

	cin >> t;

	for(int i = 0; i < t; i++) {
		int n;
		cin >> n;

		dist(n);
	}

	for(int i = 0; i < 2*t; i++) {
		cout << v[i] << " ";
	}

	return 0;
}