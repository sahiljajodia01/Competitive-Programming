#include <bits/stdc++.h>

using namespace std;

string balanced_brackets(string s) {
	stack<char> v;
	int flag = 0;

	for(int i = 0; i < s.length(); i++) {
		if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
			v.push(s[i]);
		}
		else {
			if(v.size() > 0) {
				if((s[i] == ')' && v.top() == '(') || (s[i] == '}' && v.top() == '{') || (s[i] == ']' && v.top() == '[')) {
					v.pop();
					continue;
				}
				else {
					return "NO";
				}
			}
			else {
				if(s[i] == ')' || s[i] == '}' || s[i] == ']') {
					return "NO";
				}
			}
		}
	}
	if(v.empty()) {
		return "YES";
	}
	else {
		return "NO";
	}


}

int main() {
	int t;
	string ans;

	cin >> t;

	for(int i = 0; i < t; i++) {
		string s;
		cin >> s;
		ans = balanced_brackets(s);
		cout << ans << "\n";
	}

	return 0;
}