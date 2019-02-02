#include <bits/stdc++.h>

using namespace std;

int longest_subsequence(vector<int> v) {
	int longest = 0;
	int temp = v[0];
	for(int i = 1; i < v.size(); i++) {
		if(v[i] == 1) {
			temp++;
		}
		else {
			if(temp > longest)
				longest = temp;
			temp = 0;
		}
	}
	if(temp > longest)
		longest = temp;
	return longest;
}


void chef_and_query(vector<int> v, string s, int k) {
	for(int i = 0; i < s.length(); i++) {
		if(s[i] == '!') {
			int n = v[v.size() - 1];
			for(int j = (v.size()-1); j > 0; j--) {
				v[j] = v[j-1];
			}
			v[0] = n;
			// cout << "Shifted vector: " << "\n";
			// for(int j = 0; j < v.size(); j++) {
			// 	cout << v[j] << " ";
			// }
			// cout << "\n";
		}
		else {
			int n = longest_subsequence(v);
			if(n > k)
				cout << k << "\n";
			else
				cout << n << "\n";
		}
	}
}



int main() {
	int n, q, k;

	cin >> n >> q >> k;

	vector<int> v(n);
	string s;

	for(int i = 0; i < n; i++) {
		cin >> v[i];
	}

	cin >> s;

	// int ans = longest_subsequence(v);
	// cout << ans << "\n";
	chef_and_query(v, s, k);

	return 0;
}