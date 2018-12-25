#include <bits/stdc++.h>

using namespace std;

void candiesToElephant(vector<int> v, int N, int C) {
	for(int i = 0; i < v.size(); i++) {
		C = C - v[i];
	}
	if(C >= 0) {
		cout << "Yes" << "\n";
	}
	else {
		cout << "No" << "\n";
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 0; i < t; i++) {
		int N, C, a;
		vector<int> v;
		cin >> N >> C;
		for(int j = 0; j < N; j++) {
			cin >> a;
			v.push_back(a);
		}
		candiesToElephant(v, N, C);
	}
	return 0;
}