#include <bits/stdc++.h>

using namespace std;

void night_watch(string s) {
	int sum = 0;
	if(s.length() == 1 && s[0] == '0') {
		cout << 1 << "\n";
		return;
	}
	for(int i = 0; i < s.length(); i++) {
		if(s[i] != '1') {
			if(i == 0) {
				if(s[i+1] == '0') {
					s[i] = '1';
					sum++;
				}
			}
			else if(i == s.length() - 1) {
				if(s[i-1] == '0') {
					s[i] = '1';
					sum++;
				}
			}
			else {
				if(s[i+1] == '0' && s[i-1] == '0') {
					s[i] = '1';
					sum++;
				}
			}
		}
	}
	// cout << "String after: " << s << "\n";
	cout << sum << "\n";
}


int main() {
	int t;
	cin >> t;

	while(t--) {
		int n;
		cin >> n;

		string s;
		cin >> s;

		night_watch(s);
	}

	return 0;
}