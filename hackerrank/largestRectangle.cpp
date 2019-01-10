#include <bits/stdc++.h>

using namespace std;

/////////////// This code is still not working. Will have to see the case when the height is same
/////////////// as previous height.

void largest_rectangle(vector<int> v) {
	stack<int> pos, height;
	pos.push(0);
	height.push(v[0]);

	int max = 0, i, tempPos;

	for(i = 1; i < v.size(); i++) {
		int temp = height.top();

		if(v[i] > temp) {
			pos.push(i);
			height.push(v[i]);
		}
		else if(v[i] <= temp) {

			while(!pos.empty() && v[i] <= height.top()) {
				int temp2;
				tempPos = pos.top();
				temp2 = height.top() * (i - tempPos);
				if(temp2 > max)
					max = temp2;
				height.pop();
				pos.pop();
			}
			height.push(v[i]);
			pos.push(tempPos);
		}


		// if(v[i] > v[i-1]) {
		// 	pos.push(i);
		// 	height.push(v[i]);
		// }
		// else if(v[i] <= v[i-1]) {
		// 	int temp = v[i];
		// 	if()
		// }
	}

	while(!pos.empty()) {
		int temp2;
		temp2 = height.top() * (i - pos.top());
		if(temp2 > max)
			max = temp2;

		height.pop();
		pos.pop();
	}

	cout << max << "\n";
}

int main() {

	int n;
	vector<int> v;
	cin >> n;

	for(int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		v.push_back(temp);
	}

	largest_rectangle(v);

	return 0;
}