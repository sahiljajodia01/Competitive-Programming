#include <bits/stdc++.h>

using namespace std;

void ingredient(vector<string> v) {
	map<char, int> m;

	for(int i = 0; i < v[0].length(); i++) {
		if(m.find(v[0][i]) == m.end()) {
			m[v[0][i]] = 1;
		}
	}

	// cout << "Map for 0" << "\n";
	// for(map<char, int>::iterator it = m.begin(); it != m.end(); it++) {
	// 		int second = it->second;
	// 		char first = it->first;

	// 		cout << first << " - " << second << "\n";
	// }

	for(int i = 1; i < v.size(); i++) {
		map<char, int> n;
		string s = v[i];

		for(int j = 0; j < s.length(); j++) {
			if(n.find(s[j]) == n.end()) {
				n[s[j]] = 1;
			}
		}

		for(map<char, int>::iterator it = n.begin(); it != n.end(); it++) {
			// int second = it->second;
			char first = it->first;

			if(m.find(first) == m.end()) {
				m[first] = 1;
			}
			else {
				m[first]++;
			}

			// if(second > i+1) {
			// 	it->second = i;
			// }
			// else {
			// 	it>
			// }
		}
		// cout << "Map for " << i << "\n";
		// for(map<char, int>::iterator it = m.begin(); it != m.end(); it++) {
		// 	int second = it->second;
		// 	char first = it->first;

		// 	cout << first << " - " << second << "\n";
		// }
	}

	int total = 0;
	// cout << "Size: " << v.size() << "\n";
	// cout << "Final map" << "\n";
	for(map<char, int>::iterator it = m.begin(); it != m.end(); it++) {
		// cout << it->first << " - " << it->second << "\n";
		if(it->second == v.size())
			total++;
	}

	cout << total << "\n";

}


int main() {
	int t;

	cin >> t;

	while(t--) {
		int n;
		cin >> n;

		vector<string> v(n);
		for(int i = 0; i < n; i++) {
			cin >> v[i];
		}

		ingredient(v);
	}

	return 0;
}