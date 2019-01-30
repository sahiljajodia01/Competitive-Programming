// TO BE COMPLETED
// TLE for third subtask

#include <bits/stdc++.h>

using namespace std;

void rooks(int n, vector< pair<int, int> > v) {
	vector< pair<int, int> > p;

	for(int i = 1; i <= n; i++) {
		int flag = 0;
		for(int j = 0; j < v.size(); j++) {
			// cout << "Executed 1st for" << "\n";
			if(v[j].first == i) {
				flag = 1;
				break;
			}
		}
		if(flag == 1) {
			// cout << "Executed ist flag if" << "\n";
			continue;
		}
		else {
			for(int j = 1; j <= n; j++) {
				int flag1 = 0;
				for(int k = 0; k < v.size(); k++) {
					// cout << "Executed second for" << "\n";
					if(v[k].second == j) {
						flag1 = 1;
						break;
					}
				}
				if(flag1 == 1) {
					// cout << "Executed 2nd flag if" << "\n";
					continue;
				}
				else {
					// cout << "I is: " << i << "\n";
					p.push_back(make_pair(i, j));
					v.push_back(make_pair(i, j));
					break;
				}
			}
		}
	}

	// for(int i = 0; i < n - v.size(); i++) {
	// 	int a, b;
	// 	for(int j = 1; j <= n; j++) {
	// 		int flag1 = 0;
	// 		for(int k = 0; k < v.size(); k++) {
	// 			if(i == v[k].first) {
	// 				flag1 = 1;
	// 				break;
	// 			}
	// 		}

	// 		if(flag1 == 1) {
	// 			continue;
	// 		}
	// 		else {
	// 			a = j;
	// 			break;
	// 		}
	// 	}

	// 	for(int j = 1; j <= n; j++) {
	// 		int flag1 = 0;
	// 		for(int k = 0; k < v.size(); k++) {
	// 			if(i == v[k].second) {
	// 				flag1 = 1;
	// 				break;
	// 			}
	// 		}

	// 		if(flag1 == 1) {
	// 			continue;
	// 		}
	// 		else {
	// 			b = j;
	// 			break;
	// 		}
	// 	}
	// 	p.push_back(make_pair(a, b));
	// 	v.push_back(make_pair(a, b));
	// }

	cout << p.size() << " ";
	for(int i = 0; i < p.size(); i++) {
		cout << p[i].first << " " << p[i].second << " ";
	}
	cout << "\n";
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

	while(t--) {
		vector< pair<int, int> > v;
		
		int n, k;
		scanint(n);
		scanint(k);

		// cin >> n >> k;

		while(k--) {
			int a, b;

			scanint(a);
			scanint(b);
			// cin >> a >> b;
			v.push_back(make_pair(a, b));
		}

		rooks(n, v);
	}

	return 0;
}