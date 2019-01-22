#include <bits/stdc++.h>

using namespace std;


void alora2(vector< tuple<char, char, bool> > v, string s) {
	int y = 5;

	while(y--) {
		for(int i = 0; i < v.size(); i++) {

			if(get<0>(v[i]) > get<1>(v[i])) {
				get<2>(v[i]) = true;

				for(int j = 0; j < v.size(); j++) {
					if(get<0>(v[j]) == get<1>(v[i])) {
						if(get<1>(v[j]) < get<1>(v[i])) {
							if(get<0>(v[i]) > get<1>(v[j])) {
								get<1>(v[i]) = get<1>(v[j]);
							}
						}
						// else {
						// 	get<1>(v[i]) = get<1>(v[j]);
						// }
					}
				}
				// continue;
			}
			else {
				for(int j = 0; j < v.size(); j++) {
					if(get<0>(v[j]) == get<1>(v[i])) {
						if(get<0>(v[i]) > get<1>(v[j])) {
							get<1>(v[i]) = get<1>(v[j]);
							get<2>(v[i]) = true;
						}
						else {
							get<1>(v[i]) = get<1>(v[j]);
						}
					}
				}
			}
		}
	}
	

	for(int i = 0; i < v.size(); i++) {
		cout << "First:" << get<0>(v[i]) << " " << "Second:" << get<1>(v[i]) << " " << "Third:" << get<2>(v[i]) << "\n";
	}
	string last_string;
		for(int i = 0; i < v.size(); i++) {
			if(get<2>(v[i]) == true) {
				for(int j = 0; j < s.length(); j++) {
					if(s[j] == get<0>(v[i])) {
						s[j] = get<1>(v[i]);
					}
				}
			}
		}
	



	cout << s << "\n";
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
		int n, m;
		scanint(n);
		scanint(m);
		string s;

		cin >> s;

		vector< tuple<char, char, bool> > v;

		for(int i = 0; i < m; i++) {
			char a, b;
			cin >> a >> b;
			v.push_back(make_tuple(a, b, false));
		}

		alora2(v, s);
	}



p c                                                                                                                                  
e k                                                                                                                                 
k z
b a                                                                                                                                 
z b                                                                                                                                  


}