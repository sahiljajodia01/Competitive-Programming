#include <bits/stdc++.h>

using namespace std;

void merge(vector<int> v, int beg, int mid, int end) {
	int i = beg, j = mid+1, index = beg, k;
	vector<int> temp;

	while((i <= mid) && (j <= end)) {
		if(v[i] < v[j]) {
			temp.push_back(v[i]);
			i++;
		}
		else {
			temp.push_back(v[j]);
			j++;
		}
	}
	if(i > mid) {
		while(j <= end) {
			temp.push_back(v[j]);
			j++;
		}
	}
	else {
		while(i <= mid) {
			temp.push_back(v[i]);
			i++;
		}
	}

	for(k = beg; k < temp.size(); k++) {
		v[k] = temp[k];
	}
}

void merge_sort(vector<int> v, int beg, int end) {
	int mid;
	if(beg < end) {
		mid = (beg+end)/2;
		merge_sort(v, beg, mid);
		merge_sort(v, mid+1, end);
		merge(v, beg, mid, end);
	}
}

int main() {
	int t;
	cin >> t;
	vector<int> v;

	for(int i = 0; i < t; i++) {
		int temp;
		cin >> temp;

		v.push_back(temp);
	}
	merge_sort(v, 0, v.size());

	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << "\t";
	}
	cout << "\n";

	return 0;
}