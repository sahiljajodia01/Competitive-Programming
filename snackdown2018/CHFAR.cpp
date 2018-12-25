#include <bits/stdc++.h>

using namespace std;

int sumSquares(vector<int> a) {
	int sum = 0;
	for(int i = 0; i < a.size(); i++) {
		sum += a[i]*a[i];
	}

	return sum;
}

int sumNormal(vector<int> a) {
	int sum = 0;
	for(int i = 0; i < a.size(); i++) {
		sum += a[i];
	}
	return sum;
}

int main() {
	int t;
	cin >> t;

	while(t--) {
		int N, K;
		cin >> N >> K;
		vector<int> a;
		for(int i = 0; i < N; i++) {
			int temp;
			cin >> temp;
			a.push_back(temp);
		}

		if(sumSquares(a) <= sumNormal(a)) {
			cout << "YES" << "\n";
			continue;
		}
		else {
			std::sort(a.begin(), a.end(), greater<int>());
			for(int j = 0; j < K; j++) {
				a[j] = 1;
			}

			if(sumSquares(a) <= sumNormal(a)) {
				cout << "YES" << "\n";
				continue;
			}
			else {
				cout << "NO" << "\n";
				continue;
			}
		}
	}

	return 0;
}