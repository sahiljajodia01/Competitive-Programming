#include <bits/stdc++.h>

using namespace std;

void fraud_activity(vector<int> v, int d) {
	int n = v.size();
	int count = 0;
	int frequency[201] = {};
	int pos = 0;
	for(int i = 0; i < d; i++) {
		int element = v[i];
		frequency[element]++;
		// cout << "Frequency of " << v[i] << " " << frequency[element] << "\n";
	}
	// cout << "Cumulative frequencies: " << "\n";
	for(int i = 1; i < 201; i++) {
		frequency[i] = frequency[i] + frequency[i-1];
		// cout << frequency[i] << " ";
	}
	// cout << "\n";
	for(int i = d; i < n; i++) {
		// cout << "Frequency Table: " << "\n";
		// for(int j = 0; j < 201; j++) {
		// 	cout << frequency[j] << " ";
		// }
		// cout << "\n";


		int median = 0;

		if(d % 2 == 0) {
			pos = d/2;
			int first = 0;
			int second = 0;
			for(int j = 0; j < 201; j++) {
				if(pos <= frequency[j]) {
					first = j;
					// cout << "First: " << first << "\n";
					if(pos + 1 <= frequency[j])
						second = j;
					else
						second = j+1;
					// cout << "Second: " << second << "\n";
					break;
				}
			}
			median = (first+second);
		}
		else {
			pos = (1+d)/2;
			// cout << "Pos: " << pos << "\n";
			for(int j = 0; j < 201; j++) {
				if(pos <= frequency[j]) {
					median = j;
					break;
				}
			}
			median *= 2;
		}

		// cout << "2*Median: " << median << "\n";
		
		if(v[i] >= median)
			count++;


		for(int j = 0; j < 201; j++) {
			if(j >= v[i-d]) {
				frequency[j]--;
			}
			if(j >= v[i]) {
				frequency[j]++;
			}
		}
		// for(int j = i-d; j < i; j++) {
		// 	for(int k = i-d; k < i; k++) {
		// 		if(v[j] < v[k]) {
		// 			int temp;
		// 			temp = v[j];
		// 			v[j] = v[k];
		// 			v[k] = temp;
		// 		}
		// 	}
		// }
		// cout << "Printing array: ";
		// for(int j = i-d; j < i; j++) {
		// 	cout << v[j] << " ";
		// }
		// cout << "\n";

		// if(d % 2 != 0) {
		// 	median = v[(i-d+i)/2];
		// }
		// else {
		// 	int first = v[(i-d+i)/2];
		// 	int second = v[(i-d+i)/2 + 1];
		// 	median = (first + second)/2;
		// }

		// // cout << "Median: " << median << "\n";

		// if(v[i] >= 2*median) {
		// 	count++;
		// }
	}

	cout << count << "\n";
}

int main() {
	int n, d;
	vector<int> v;

	cin >> n >> d;

	for(int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		v.push_back(temp);
	}

	fraud_activity(v, d);

	return 0;
}