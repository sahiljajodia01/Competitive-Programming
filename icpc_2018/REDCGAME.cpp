#include <bits/stdc++.h>

using namespace std;

bool find(vector<int> arr, int j) {
	for(int i = 0; i < arr.size(); i++) {
		if(arr[i] == j) {
			return true;
		}
	}
	return false;
}


void redcgame(vector<int> a, int k) {
	int sum = 0;
	int l = -1, s = -1;
	map<int, vector<int> > m;
	for(int n = 0; n < a.size(); n++) {
		
		map<int, vector<int> >::iterator it2 = m.begin();

		while(it2 != m.end()) {
			int first = it2->first;
			vector<int> second = it2->second;
			cout << "First: " << first;
			a[first]++;
			for(int z = 0; z < second.size(); z++) {
				a[second[z]]++;
			}
			it2++;
		}
		
		for(int i = 0; i < a.size() - 1; i++) {
			for(int j = i+1; j < a.size(); j++) {
				if(min(a[i], a[j]) > k && !find(m[i], j)) {
					a[i]--;
					a[j]--;
					
					
					m[i].push_back(j);
				}
			}
		}

		int sum_current = 0;
		for(int m = 0; m < a.size(); m++) {
			sum_current += a[m];
		}

		if(sum_current >= sum) {
			cout << "Sum: " << sum << "\n";
			sum = sum_current;
		}

	}
	

	if(sum == 0) {
		for(int i = 0; i < a.size(); i++) {
			sum += a[i];
		}
	}

	cout << sum << "\n";
}

int main() {
	int t;
	cin >> t;


	for(int i = 0; i < t; i++) {
		int n, k;
		vector<int> a;

		cin >> n >> k;

		for(int j = 0; j < n; j++) {
			int m;
			cin >> m;
			a.push_back(m);
		}

		redcgame(a, k);
	}
}