#include <bits/stdc++.h>

using namespace std;


void typing(map<string, int> m) {
	map<string, int>::iterator it2 = m.begin();
	bool flag = false;
	float total = 0;
	while(it2 != m.end()) {
		string s = it2->first;
		int v = it2->second;
		float time = 0;
		time += 0.2;
		if(v == 1) {
			for(int i = 1; i < s.length(); i++) {
				if((s[i-1] == 'd' || s[i-1] == 'f')) {

					if(s[i] == 'd' || s[i] == 'f') {
						time += 0.4;
					}
					else {
						time += 0.2;
					}

				}
				else {
					if(s[i] == 'd' || s[i] == 'f') {
						time += 0.2;
					}
					else {
						time += 0.4;
					}
				}
			}
		}
		else {
			for(int i = 1; i < s.length(); i++) {
				if((s[i-1] == 'd' || s[i-1] == 'f')) {

					if(s[i] == 'd' || s[i] == 'f') {
						time += 0.4;
					}
					else {
						time += 0.2;
					}

				}
				else {
					if(s[i] == 'd' || s[i] == 'f') {
						time += 0.2;
					}
					else {
						time += 0.4;
					}
				}
			}
			for(int j = 0; j < v - 1; j++) {
				time += time / 2;
			}
		}
		total += time;
		it2++;
	}
	total *= 10;

	cout << total << "\n";
}


int main() {

	int T;
	cin >> T;

	for(int i = 0; i < T; i++) {
		int N;
		cin >> N;
		map<string, int> map1;
		for(int j = 0; j < N; j++) {
			string s;

			cin >> s;

			if(map1.find(s) == map1.end()) {
				map1[s] = 1;
			}
			else {
				map1[s]++;
			}
		}

		typing(map1);
	}

	return 0;
}
