#include <bits/stdc++.h>

using namespace std;

void pairs(vector<int> v, int k) {
	map<int, int> m;

	for(int i = 0; i < v.size(); i++) {
		int temp = v[i];
		if(m.find(temp) == m.end()) {
			m[temp] = 1;
		}
		else {
			m[temp]++;
		}
	}


	map<int, int>::iterator it = m.begin();

	while(it != m.end()) {
		// cout << it->first << "->" << it->second << "\n";
		it++;
	}
	it = m.begin();
	int count = 0;
	while(it != m.end()) {
		int first = it->first;
		int second = it->second;

		if(m.find(first + k) != m.end()) {
			// cout << "Inside 1st if" << "\n";
			count++;
		}
		it++;
	}

	cout << count << "\n";
}

int main() {

	int n, k;
	vector<int> v;
	cin >> n >> k;

	for(int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		v.push_back(temp);
	}

	pairs(v, k);
	return 0;
}