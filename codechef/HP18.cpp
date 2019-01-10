#include <bits/stdc++.h>

using namespace std;


void hp18(vector<int> v, int a, int b) {
		if(a == b) {
			int count = 0;
			for(int i = v.size() - 1; i >= 0; i--) {
				if(v[i] % a == 0) {
					count++;
				}
			}
			// if(count % 2 == 0) {
			// 	cout << "ALICE" << "\n";
			// }
			// else {
			// 	cout << "BOB" << "\n";
			// }
			// break;
			if(count > 0)
				cout << "BOB" << "\n";
			else
				cout << "ALICE" << "\n";
		}
		else {
			int count1 = 0, count2 = 0, count3 = 0;
				for(int i = v.size() - 1; i >= 0; i--) {
					if(v[i] % a == 0 && v[i] % b == 0) {
						v.erase(v.begin() + i);
						count1++;
					}
					else if(v[i] % a == 0) {
						count3++;
					}
				}

				for(int i = v.size() - 1; i >= 0; i--) {
					if(v[i] % b == 0) {
						v.erase(v.begin() + i);
						count2++;
					}
				}
				if(count1 > 0) {
					count3++;
				}

				if(count2 >= count3) {
					cout << "ALICE" << "\n";
				}
				else {
					cout << "BOB" << "\n";
				}



			// cout << "Inside else " << "\n";
			// int flag = -1;
			// int flag2 = 0;
			// int count1 = 0;
			// int count2 = 0;
			// while(true) {
			// 	flag2 = 0;
			// 	// cout << "Size of vector: " << v.size() << "\n";
			// 	for(int i = v.size() - 1; i >= 0; i--) {
			// 		// cout << v[i] << "\n";
			// 		if((v[i] % a == 0 && flag == -1) || (v[i] % b == 0 && flag == 1)) {
			// 			// cout << "Ele: " << v[i] << "\n";
			// 			v.erase(v.begin() + i);
			// 			flag2 = 1;
			// 			if(flag == -1)
			// 				count1++;
			// 			else
			// 				count2++;
			// 			break;
			// 		}
			// 		// else {
			// 		// 	cout << "Inside second else" << "\n";
						
			// 		// }
			// 	}
			// 	if(flag2 == 0) {
			// 		break;
			// 	}
			// 	flag *= -1;
			// }
			// if(flag == -1) {
			// 	cout << "ALICE" << "\n";
			// }
			// else {
			// 	cout << "BOB" << "\n";
			// }
		}
}


int main() {
	int t;

	cin >> t;

	for(int i = 0; i < t; i++) {
		int n, a, b;
		vector<int> v;

		cin >> n >> a >> b;

		for(int j = 1; j <= n; j++) {
			// v.push_back(j);
			int temp;
			cin >> temp;
			v.push_back(temp);
		}

		hp18(v, a, b);
	}


	return 0;
}