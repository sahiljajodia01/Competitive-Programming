#include <bits/stdc++.h>

using namespace std;


void two_sum(vector<int> v, int money) {
	map<int, int> m;
	// const max = numeric_limits<int>::max();
	// int arr[max];

	// for(int i = 0; i < max; i++) {
	// 	arr[i] = -1;
	// }

	for(int i = 0; i < v.size(); i++) {
		int temp = v[i];
		if(m.find(temp) == m.end()) {
			m[temp] = 1;
		}
		else {
			m[temp]++;
		}
	}

	map<int, int>::iterator it = m.begin();

	while(it != m.end()) {
		// cout << it->first << "->" << it->second << "\n";
		it++;
	}

	int first_index = -1, second_index = -1;
	it = m.begin();
	while(it != m.end()) {
		int first = it->first;
		int second = it->second;
		// cout << "First: " << first << "\n";
		// cout << "Second: " << second << "\n";
		// int first_index = first;

		if(m.find(money-first)->first == first) {
			// cout << "Inside if" << "\n";
			if(second > 1) {
				// int i, k;
				// for(i = 0; i < v.size(); i++) {
				// 	if(v[i] == first) {
				// 		first_index = v[i];
				// 		break;
				// 	}
				// }
				// for(k = i; k < v.size(); k++) {
				// 	if(v[i] == first) {
				// 		second_index = v[i];
				// 		break;
				// 	}
				// }

				vector<int>::iterator it1 = find(v.begin(), v.end(), first);
				int first_index = distance(v.begin(), it1);

				vector<int>::iterator it2 = find(it1+1, v.end(), first);
				int second_index = distance(v.begin(), it2);
				// cout << "First index: " << first_index << "\n";
				// cout << "Second index: " << second_index << "\n";
				cout << first_index+1 << " " << second_index+1 << "\n";
			}
			break;

		}
		else if(m.find(money-first) == m.end()) {
			it++;
			continue;
		}
		else {
			vector<int>::iterator it1 = find(v.begin(), v.end(), first);
			int index1 = distance(v.begin(), it1);

			vector<int>::iterator it2 = find(v.begin(), v.end(), money-first);
			int index2 = distance(v.begin(), it2);

			first_index = index1 < index2 ? index1 : index2;
			second_index = index1 > index2 ? index1 : index2;

			cout << first_index+1 << " " << second_index+1 << "\n";
			break;
		}
		it++;
	}
}


int main() {
	int t;
	cin >> t;

	for(int i = 0; i < t; i++) {
		int money, size;
		cin >> money;
		cin >> size;
		vector<int> v;

		for(int j = 0; j < size; j++) {
			int temp;
			cin >> temp;
			v.push_back(temp);
		}

		two_sum(v, money);
	}

	return 0;
}