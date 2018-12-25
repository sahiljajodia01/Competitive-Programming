#include <bits/stdc++.h>

using namespace std;

bool exists(vector<int> a, int k) {
	for(int i = 0; i < a.size(); i++) {
		if(k == a[i]) {
			return true;
		}
	}
	return false;
}

int main() {
	int t;

	cin >> t;

	while(t--) {
		int N, M, K, L;

		cin >> N >> M >> K >> L;

		vector<int> a;
		vector<int> q;

		for(int i = 0; i < N; i++) {
			int temp;
			cin >> temp;
			a.push_back(temp);
		}

		for(int i = 0; i < M; i++) {
			q.push_back(1);
		}

		int min_size = q.size();
		int min_time = K;

		for(int i = 1; i <= K; i++) {
			// cout << "i = " << i << " erase = " << (i) % L << "\n";
			if((i) % L == 0) {
				q.erase(q.begin());
			}

			int current_size = q.size();
			// cout << "Current size: " << current_size << "\n";

			if(exists(a, i)) {
				q.push_back(1);
			}
			if(current_size <= min_size) {
				min_size = current_size;
				min_time = i;
			}
		}

		int t = 0;
		while(t <= min_time - L) {
			t += L;
		}
		int time = 0;

		for(int i = 0; i < min_size; i++) {
			time += L;
		}
		time = time + L - (min_time - t);
		cout << time << "\n";
	}

	return 0;
}