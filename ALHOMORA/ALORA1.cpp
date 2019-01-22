#include <bits/stdc++.h>

using namespace std;

void alora1(vector<int> v, int n) {
	map<int, int> m;

	for(int i = 0; i < n; i++) {
		if(m.find(v[i]) == m.end()) {
			m[v[i]] = 1;
		}
		else {
			m[v[i]]++;
		}
	}


	for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
		// cout << it->second << "\n";
		if(it->second > 1) {
			cout << "yes" << "\n";
			return;
		}
	}
	cout << "no" << "\n";
}

inline void scanint(int &x) {
    register int c = getchar_unlocked();
    x = 0;
    int neg = 0;
 
    for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());
 
    if(c=='-') {
        neg = 1;
        c = getchar_unlocked();
    }
 
    for(; c>47 && c<58 ; c = getchar_unlocked()) {
        x = (x<<1) + (x<<3) + c - 48;
    }
 
    if(neg)
        x = -x;
}

int main() {
	int t;

	scanint(t);

	for(int i = 0; i < t; i++) {
		int n;
		vector<int> v;

		scanint(n);

		for(int j = 0; j < n; j++) {
			int temp;
			scanint(temp);

			v.push_back(temp);
		}

		alora1(v, n);
	}
}