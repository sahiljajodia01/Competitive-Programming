#include <bits/stdc++.h>

using namespace std;


map<char, int> loop(map<char, int> m, string s) {
	for(int i = 0; i < s.length(); i++) {
		char c = s[i];
		if(m.find(c) == m.end()) {
			m[c] = 1;
		}
		else {
			m[c]++;
		}
	}
	return m;
}

void lapindrome(string s) {
	string left, right;
	int len = s.length();
	int mid = len/2;
	map<char, int> m;
	if(len % 2 == 0) {
		left = s.substr(0, mid);
		right = s.substr(mid, len - mid);
	}
	else {
		left = s.substr(0, mid);
		right = s.substr(mid+1, len - mid+1);
	}
	m = loop(m, left);
	m = loop(m, right);
	map<char, int>::iterator it2 = m.begin();
	bool flag = false;
	while(it2 != m.end()) {
		if(it2->second %2 != 0) {
			flag = true;
			break;
		}
		it2++;
	}
	if(flag == true) {
		cout << "NO" << "\n";
	}
	else {
		cout << "YES" << "\n";
	}
}

int main() {
	int t;

	cin >> t;

	for(int i = 0; i < t; i++) {
		string s;
		cin >> s;
		lapindrome(s);
	}
	return 0;
}