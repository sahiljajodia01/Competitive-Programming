#include <bits/stdc++.h>

using namespace std;



void robogame(string s) {

	int range_before, range_after, index;
	int count = 0;
	bool flag = true;

	for(int i = 0; i < s.length(); i++) {
		if(s[i] != '.' && count == 0) {
			index = i;
			int value = s[i] - '0';
			if(index - value < 0) {
				range_before = 0;
			}
			else {
				range_before = index - value;
			}

			if((index + value) > (s.length() - 1)) {
				range_after = s.length() - 1;
			}
			else {
				range_after = index + value;
			}

			count++;
		}


		else if(s[i] != '.' && count > 0 ){
			index = i;
			int value = s[i] - '0';
			if(index - value <= range_after) {
				cout << "unsafe" << "\n";
				flag = false;
				break;
			}
			else {
				if(index - value < 0) {
				range_before = 0;
				}
				else {
					range_before = index - value;
				}


				if((index + value) > (s.length() - 1)) {
					range_after = s.length() - 1;
				}
				else {
					range_after = index + value;
				}

			}
			count++;
		}
	}

	if(flag == true) {
		cout << "safe" << "\n";
	}

}

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; i++) {
		string s;
		cin >> s;
		robogame(s);
	}


	return 0;
}