#include <bits/stdc++.h>

using namespace std;

void sequence_game(vector<int> v) {
	// if(v.size() == 1 || v.size() == 2) {
	// 	cout << "Poor Chef" << "\n";
	// 	return;
	// }


	// map<int, int> m;

	// for(int i = 0; i < v.size(); i++) {
	// 	if(m.find(v[i]) == m.end()) {
	// 		m[v[i]] = 1;
	// 	}
	// 	else {
	// 		m[v[i]]++;
	// 	}
	// }

	set<int> index(v.begin(), v.end());
	set<int> index_of_index;

	for(set<int>::iterator it = index.begin(); it != index.end(); ++it) {
		index_of_index.insert(v[*it - 1]);
	}

	if(index.size() > index_of_index.size()) {
		cout << "Truly Happy" << "\n";
	}
	else {
		cout << "Poor Chef" << "\n";
	}


	// This is a wrong approach
	// int flag = 0;
	// for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
	// 	int second = it->second;

	// 	if(second > 1) {
	// 		cout << "Inside 1st if" << "\n";
	// 		int first = it->first;
	// 		vector<int> indexes;

	// 		for(int i = 0; i < v.size(); i++) {
	// 			if(v[i] == first) {
	// 				indexes.push_back(i);
	// 			}
	// 		}

	// 		cout << "Indexes array: " << "\n";
	// 		for(int i = 0; i < indexes.size(); i++) {
	// 			cout << indexes[i] << " ";
	// 		}
	// 		cout << "\n";

	// 		for(int i = 0; i < indexes.size() - 1; i++) {
	// 			for(int j = i+1; j < indexes.size(); j++) {
	// 				cout << "i: " << i << "\t" << "j: " << j << "\n";
	// 				cout << "v[indexes[i] + 1]: " << v[indexes[i] + 1] << "\t" << "v[indexes[j] + 1]: " << v[indexes[j] + 1] << "\n";
	// 				if(v[indexes[i] + 1] != v[indexes[j] + 1]) {
	// 					cout << "Inside if if" << "\n";
	// 					// cout << "Poor Chef" << "\n";
	// 					// return;
	// 					flag = 1;
	// 				}
	// 				// else {
	// 				// 	// cout << "Inside if else" << "\n";
	// 				// 	cout << "Truly Happy" << "\n";
	// 				// 	return;
	// 				// }
	// 			}
	// 		}
	// 	}
	// 	else {
	// 		cout << "Inside else" << "\n";
	// 	}
	// }
	// cout << "Poor Chef" << "\n";


	// Brute force Approach
	// int flag = 0;
	// for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
	// 	for(map<int, int>::iterator it1 = m.begin(); it1 != m.end(); it1++) {
	// 		int first = it->first;
	// 		int second = it1->first;

	// 		if(first != second) {
	// 			if(v[first - 1] == v[second - 1]) {
	// 				flag = 1;
	// 			}
	// 		}
			
	// 	}
	// }


	// Brute force Approach
	// int flag = 0;
	// for(int i = 0; i < v.size() - 1; i++) {
	// 	for(int j = i+1; j < v.size(); j++) {
	// 		if(v[i] != v[j]) {
	// 			if(v[v[i]-1] == v[v[j]-1]) {
	// 				flag = 1;
	// 			}
	// 		}
	// 	}
	// }

	// if(flag == 1) {
	// 	cout << "Truly Happy" << "\n";
	// }
	// else {
	// 	cout << "Poor Chef" << "\n";
	// }
}

int main() {
	int t;
	cin >> t;

	while(t--) {
		int n;
		cin >> n;
		vector<int> v;

		for(int i = 0; i < n; i++) {
			int temp;
			cin >> temp;

			v.push_back(temp);
		}

		sequence_game(v);
	}

	return 0;
}