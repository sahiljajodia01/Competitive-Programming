#include <bits/stdc++.h>

using namespace std;

void beautiful_garland(string s) {
	int n = s.length();


	// MY FIRST TRY: UNSUCCESSFULL
	// char arr[n+1];

	// strcpy(arr, s.c_str());
	// int count = 0;
	// char prev = arr[0];
	// int flag = 0;
	// char prev_char = '';
	// for(int i = 1; i < arr.length(); i++) {
	// 	if(count > 2) {
	// 		prev_char = '';
	// 		break;
	// 	}
	// 	if(arr[i] == prev) {
	// 		prev_char = arr[i];
	// 		count++;
	// 	}
	// 	else {
	// 		prev = '';
	// 		count = 0;
	// 	}
	// }



	// MY SECOND TRY: UNSUCCESSFULL
	// string r = "RR";
	// string g = "GG";

	// int found_r = s.find(r);
	// int found_g = s.find(g);

	// // cout << "R Pos: " << found_r << "\n";
	// // cout << "G Pos: " << found_g << "\n";
	// int flag = 0;
	// for(int i = 1; i < s.length(); i++) {
	// 	if(s[i] == s[i-1]) {
	// 		flag = 1;
	// 	}
	// }
	// if(flag == 1) {
	// 	if(found_r == -1 || found_g == -1) {
	// 		cout << "no" << "\n";
	// 	}
	// 	else if(found_r < found_g) {
	// 		string sub = s.substr(found_r+1, found_g - found_r);
	// 		// cout << "Substring: " << sub << "\n";
	// 		reverse(sub.begin(), sub.end());
	// 		// cout << "Reverse Sub: " << sub << "\n";
	// 		int count = 0;
	// 		for(int k = found_r+1; k <= found_g; k++) {
	// 			s[k] = sub[count];
	// 			count++;
	// 		}
	// 		// cout << "Original after reverse: " << s << "\n";
	// 		int flag1 = 0;
	// 		for(int i = 1; i < s.length(); i++) {
	// 			if(s[i] == s[i-1]) {
	// 				flag1 = 1;
	// 				break;
	// 			}
	// 		}
	// 		if(flag1 == 0) {
	// 			cout << "yes" << "\n";
	// 		}
	// 		else {
	// 			cout << "no" << "\n";
	// 		}

	// 	}
	// 	else {
	// 		string sub = s.substr(found_g+1, found_r - found_g);
	// 		// cout << "Substring: " << sub << "\n";
	// 		reverse(sub.begin(), sub.end());
	// 		// cout << "Reverse Sub: " << sub << "\n";
	// 		int count = 0;
	// 		for(int k = found_g+1; k <= found_r; k++) {
	// 			s[k] = sub[count];
	// 			count++;
	// 		}
	// 		// cout << "Original after reverse: " << s << "\n";
	// 		int flag1 = 0;
	// 		for(int i = 1; i < s.length(); i++) {
	// 			if(s[i] == s[i-1]) {
	// 				flag1 = 1;
	// 				break;
	// 			}
	// 		}
	// 		if(flag1 == 0) {
	// 			cout << "yes" << "\n";
	// 		}
	// 		else {
	// 			cout << "no" << "\n";
	// 		}
	// 	}
	// }
	// else {
	// 	cout << "yes" << "\n";
	// }


	// AN AMAZINGLY AWESOME SOLUTION!!
	vector<int> v;
	for(int i = 0; i < n; i++) {
		if(s[i] == s[(i+1)%n]) {
			v.push_back(s[i]);
		}
	}

	if(v.empty()) {
		cout << "yes" << "\n";
	}
	else if(v.size() != 2) {
		cout << "no" << "\n";
	}
	else if(v.size() == 2) {
		if(v[0] != v[1]) {
			cout << "yes" << "\n";
		}
		else {
			cout << "no" << "\n";
		}
	}
	
}

int main() {
	int t;
	cin >> t;

	for(int i = 0; i < t; i++) {
		string s;

		cin >> s;

		beautiful_garland(s);
	}
	return 0;
}