#include <bits/stdc++.h>

using namespace std;

vector<int> min_stations(vector<int> b, int m, int V) {
	vector<int> table;
	table.push_back(0);
	for(int i = 1; i <= V; i++) {
		table.push_back(INT_MAX);
	}

	for(int i = 1; i <= V; i++) {
		for(int j = 0; j < m; j++) {
			if(b[j] <= i) {
				int temp = table[i - b[j]];
				if(temp != INT_MAX && temp + 1 < table[i]) {
					table[i] = temp + 1;
				}
			}
		}
	}

	return table;
}


int pizza_dil(vector<int> a, vector<int> b) {
	int max_sum = *max_element(a.begin(), a.end());
	int sum = 0;
	vector<int> sum_table = min_stations(b, b.size(), max_sum);
	// int len = (sizeof(sum_table)/sizeof(*sum_table));

	for(int i = 0; i < a.size(); i++) {
		sum += sum_table[a[i]];
	}

	return sum;
}

int main() {
	int t;

	cin >> t;

	while(t--) {
		int n;
		cin >> n;
		int ans;
		vector<int> a, b;

		for(int i = 0; i < n; i++) {
			int temp;
			cin >> temp;
			a.push_back(2*temp);
		}

		for(int i = 0; i < n; i++) {
			int temp;
			cin >> temp;
			b.push_back(temp);
		}

		ans = pizza_dil(a, b);
		cout << ans << "\n";
	}
	return 0;
}