#include <bits/stdc++.h>

using namespace std;

void mgame(int n, int p) {
	// map<long, long> m;
	// for(long i = 1; i <= p; i++) {
	// 	for(long j = 1; j <= p; j++) {
	// 		for(long k = 1; k <= p; k++) {
	// 			long score = (((n%i)%j)%k)%n;
	// 			if(m.find(score) == m.end()) {
	// 				m[score] = 1;
	// 			}
	// 			else {
	// 				m[score]++;
	// 			}
	// 			cout << "( " << i << " " << j << " " << k << " ) = " << score << "\n";
	// 		}
	// 	}
	// }

	// map<long, long>::iterator it = m.begin();

	// while(it != m.end()) {
	// 	cout << it->first << " - " << it->second << "\n";
	// 	it++;
	// }


	long long max = 0, maxNum = 0, ans;
    // max = n/2 - 1;
   	max = n%(n/(int)2+1);
    maxNum = n/2 + 1;
    if(max == 0) {
    	ans = (p*p*p);
    }
    else {
    	ans = (((p-max)*(p-max)) + ((p-n)*(p-max)) + ((p-n)*(p-n)));
    }
    cout << ans << "\n";
}


// inline void scanint(int &x) {
//     register int c = getchar_unlocked();
//     x = 0;
//     int neg = 0;
 
//     for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());
 
//     if(c=='-') {
//         neg = 1;
//         c = getchar_unlocked();
//     }
 
//     for(; c>47 && c<58 ; c = getchar_unlocked()) {
//         x = (x<<1) + (x<<3) + c - 48;
//     }
 
//     if(neg)
//         x = -x;
// }

int main() {
	int t;

	cin >> t;

	for(int i = 0; i < t; i++) {
		int n, p;

		// scanint(n);
		// scanint(p);
		cin >> n >> p;

		mgame(n, p);


	}
}