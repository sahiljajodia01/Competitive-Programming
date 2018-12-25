#include <bits/stdc++.h>

using namespace std;

vector<int> v;

void dist(int n) {
	int num, den;

	num = ;
	den = pow(2, n);

	v.push_back(num);
	v.push_back(den);
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