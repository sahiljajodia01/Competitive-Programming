#include <bits/stdc++.h>

using namespace std;

int a[5001][5001];

int common_child(string s1, string s2, int m, int n, int a[5001][5001]) {
	if(m == 0 || n == 0) {
		return 0;
	}
	if(a[m][n] != -1) {
		return a[m][n];
	}
	else {
		if(s1[m-1] == s2[n-1]) {
			a[m][n] = 1 + common_child(s1, s2, m-1, n-1, a);
		}
		else {
			a[m][n] =  max(common_child(s1, s2, m-1, n, a), common_child(s1, s2, m, n-1, a));
		}
		return a[m][n];
	}
}

int main() {
	int ans;
	string s1;
	string s2;
	// cout << "Hello" << "\n";

	for(int i = 0; i < 5001; i++) {
		for(int j = 0; j < 5001; j++) {
			a[i][j] = -1;
		}
	}
	int m, n;

	cin >> s1;
	cin >> s2;

	m = s1.length();
	n = s2.length();


	ans = common_child(s1, s2, m, n, a);

	cout << ans << "\n";

	return 0;
}