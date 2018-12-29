#include <bits/stdc++.h>

using namespace std;

void triple_sum(vector<int> a, vector<int> b, vector<int> c) {
	// sort(a.begin(), a.end());
	// sort(b.begin(), b.end());
	// sort(c.begin(), c.end());

	int count = 0;

	// cout << "Array A: " << "\n";
	// for(int i = 0; i < a.size(); i++) {
	// 	cout << a[i] << " ";
	// }
	// cout << "\n";

	// cout << "Array B: " << "\n";
	// for(int i = 0; i < b.size(); i++) {
	// 	cout << b[i] << " ";
	// }
	// cout << "\n";

	// cout << "Array C: " << "\n";
	// for(int i = 0; i < c.size(); i++) {
	// 	cout << c[i] << " ";
	// }
	// cout << "\n";

	set<int> s1(a.begin(), a.end());
	a.assign(s1.begin(), s1.end());

	set<int> s2(b.begin(), b.end());
	b.assign(s2.begin(), s2.end());

	set<int> s3(c.begin(), c.end());
	c.assign(s3.begin(), s3.end());

	map<int, int> m;

	// for(int i = 0; i < b.size(); i++) {
	// 	if(m.find(b[i]) == m.end()) {
	// 		m[b[i]] = 1;
	// 	}
	// }

	for(int i = 0; i < b.size(); i++) {
		int temp = b[i];
		cout << "Temp: " << temp << "\n";
		int a_index = 0, c_index = 0;

		///////////////// Right now giving TLE on 2 test cases....mayble because of the custom 
		///////////////// logic below. We can also use upper_bound function available in c++
		///////////////// which will maybe solve the TLE. Also i can try and imporve the custom
		///////////////// logic to solve TLE.

		for(int j = 0; j < a.size(); j++) {
			if(j == a.size() - 1 && temp >= a[j]) {
				a_index = j+1;
				break;
			}
			if(a[j] > temp) {
				a_index = j;
				break;
			}
		}

		for(int j = 0; j < c.size(); j++) {
			if(j == c.size() - 1 && temp >= c[j]) {
				c_index = j+1;
				break;
			}
			if(c[j] > temp) {
				c_index = j;
				break;
			}
		}

		cout << "A index: " << a_index << "\n";
		cout << "C index: " << c_index << "\n";
		count += a_index * c_index;
	}


	cout << count << "\n";
}

int main() {
	int la, lb, lc;
	vector<int> a, b, c;

	cin >> la >> lb >> lc;

	for(int i = 0; i < la; i++) {
		int temp;
		cin >> temp;
		a.push_back(temp);
	}

	for(int i = 0; i < lb; i++) {
		int temp;
		cin >> temp;
		b.push_back(temp);
	}

	for(int i = 0; i < lc; i++) {
		int temp;
		cin >> temp;
		c.push_back(temp);
	}

	triple_sum(a, b, c);

	return 0;
}