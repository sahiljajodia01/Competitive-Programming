#include <bits/stdc++.h>

using namespace std;

int main() {

	int t;
	cin >> t;

	while(t--) {
		int n;
		cin >> n;
		vector<int> v;

		// for(int i = 1; i <= n; i++) {
		// 	int temp;
		// 	cout << "1 " << i << " " << i << " " << i << endl;
		// 	cin >> temp;
		// 	v.push_back(temp);
		// }

		// cout << "2 ";
		// for(int i = 0; i < n; i++) {
		// 	if(i != n-1)
		// 		cout << v[i] << " ";
		// 	else
		// 		cout << v[i] << endl;
		// }

		// int result;
		// if(result == 1) {

		// }

		if(n % 2 == 0) {
			int mid = (1+n)/2;
			for(int i = 1; i <= mid - 2; i+=3) {
				int temp;
				int first = i;
				int second = i+1;
				int thrid = i+2;
				cout << "1 " << first << " " << second << " " << third << endl;
				cin >> temp;
				v.push_back(temp);
			}
		}


	}

	return 0;
}