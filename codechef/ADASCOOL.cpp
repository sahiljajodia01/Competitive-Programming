#include <bits/stdc++.h>

using namespace std;

void adascool(int n, int m) {
	if(n % 2 != 0 && m % 2 != 0) {
		cout << "NO" << "\n";
	}
	else {
		cout << "YES" << "\n";
	}
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

		adascool(n, m);
	}


	return 0;
}