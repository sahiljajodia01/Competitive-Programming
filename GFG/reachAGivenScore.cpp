#include <bits/stdc++.h>

using namespace std;


// This is wrong.
// int reach_score(int n, int a[], int sum) {
//     // if(n == 3 || n == 5 || n == 10) {
        
//     // }
//     else if(n < 3) {
//         return 0;
//     }

// 	t[n] += 0;

//     return reach_score(n-3) + reach_score(n-5) + reach_score(n-10);
    
// }


// Using iterative approach
int reach_score(int n) {
	int t[n+1];

	memset(t, 0, sizeof(t));

	t[0] = 1;

	for(int i = 3; i <= n; i++) {
		t[i] += t[i-3];
	}
	for(int i = 5; i <= n; i++) {
		t[i] += t[i-5];
	}
	for(int i = 10; i <= n; i++) {
		t[i] += t[i-10];
	}

	return t[n];
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        // int ans = reach_score(n);
		int tb[n+1];
		int sum = 0;
		int ans = reach_score(n);

        cout << ans << "\n";
    }

    return 0;
}