#include <bits/stdc++.h>

using namespace std;

void chefAndPoet(int X, int Y, int K, int N, vector<vector<int> > v) {
	X = X - Y;
		// cout << "X: " << X << "\n";
	int flag = 0;
	for(int i = 0; i < v.size(); i++) {
		if(X >= v[i][0] && K <= v[i][1]) {
			flag = 1;
			break;
		}
	}

	if(flag == 1) {
		cout << "LuckyChef" << "\n"; 
	}
	else {
		cout << "UnluckyChef" << "\n";
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 0; i < t; i++) {
		int X, Y, K, N;
		vector<vector<int> > v;

		cin >> X >> Y >> K >> N;

		for(int j = 0; j < N; j++) {
			vector<int> row;
			for(int k = 0; k < 1; k++) {
				int P, C;
				cin >> P >> C;
				row.push_back(P);
				row.push_back(C);
			}
			v.push_back(row);
		}
		chefAndPoet(X, Y, K, N, v);
	}

	return 0;
}