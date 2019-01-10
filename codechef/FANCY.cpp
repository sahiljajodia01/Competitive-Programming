#include <bits/stdc++.h>

using namespace std;

void fancy(string s) {
	// string str (" not ");
	int found = s.find(" not ");
	int found1 = s.find("not ");
	size_t found2 = s.rfind(" not");

	// cout << "found: " << found << "\n";
	// cout << "found1: " << found1 << "\n";
	// cout << "found2: " << found2 << "\n";
	if(found != -1) {
		cout << "Real Fancy" << "\n";
	}
	else if(found1 == 0) {
		cout << "Real Fancy" << "\n";
	}
	else if(found2 == s.length()-4) {
		cout << "Real Fancy" << "\n";
	}
	else {
		cout << "regularly fancy" << "\n";
	}
}

int main() {
	int t;
	cin >> t;
	cin.ignore();
	for(int i = 0; i < t; i++) {
		char s[100];
		// scanf ("%[^\n]%*c", s);
		cin.getline(s, sizeof(s));
		string st(s);
		// cout << "String: " << s << "\n";
		fancy(st);
	}

	return 0;
}