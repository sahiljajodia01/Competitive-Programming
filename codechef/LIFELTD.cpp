#include <bits/stdc++.h>

using namespace std;

void temp_ltd(int a[3][3]) {
	int flag = 0;
	for(int i = 0; i < 2; i++) {
		for(int j =0; j < 2; j++) {
			if(a[i][j] == 'l' && a[i+1][j] == 'l' && a[i+1][j+1] == 'l') {
				cout << "yes" << "\n";
				flag = 1;
				break;
			}
		}
		if(flag == 1)
			break;
	}
	if(flag == 0)
		cout << "no" << "\n";
}


int main() {
	int t;
	cin >> t;

	while(t--) {
		int a[3][3];
		for(int i = 0; i < 3; i++) {
			string temp;
			cin >> temp;
			for(int j = 0; j < 3; j++) {
				a[i][j] = temp[j];
			}
		}
		temp_ltd(a);

	}
	return 0;
}