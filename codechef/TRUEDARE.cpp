#include <bits/stdc++.h>

using namespace std;

void truthdare(vector<int> tr, vector<int> dr, vector<int> ts, vector<int> ds) {
	int flag1, flag2;
	for(int i = 0; i < ts.size(); i++) {
		flag1 = 0;
		for(int j = 0; j < tr.size(); j++) {
			if(ts[i] == tr[j]) {
				flag1 = 1;
				break;
			}
		}
		if(flag1 == 0) {
			break;
		}
	}

	for(int i = 0; i < ds.size(); i++) {
		flag2 = 0;
		for(int j = 0; j < dr.size(); j++) {
			if(ds[i] == dr[j]) {
				flag2 = 1;
				break;
			}
		}
		if(flag2 == 0) {
			break;
		}
	}

	if(flag1 == 1 && flag2 == 1) {
		cout << "yes" << "\n";
	}
	else {
		cout << "no" << "\n";
	}
}

int main() {
	int t;

	cin >> t;

	for(int i = 0; i < t; i++) {
		int tr, dr, ts, ds;
		vector<int> t_ram, d_ram, t_shyam, d_shyam;

		cin >> tr;

		for(int j = 0; j < tr; j++) {
			int temp;
			cin >> temp;
			t_ram.push_back(temp);
		}

		cin >> dr;

		for(int j = 0; j < dr; j++) {
			int temp;
			cin >> temp;
			d_ram.push_back(temp);
		}

		cin >> ts;

		for(int j = 0; j < ts; j++) {
			int temp;
			cin >> temp;
			t_shyam.push_back(temp);
		}

		cin >> ds;

		for(int j = 0; j < ds; j++) {
			int temp;
			cin >> temp;
			d_shyam.push_back(temp);
		}		

		truthdare(t_ram, d_ram, t_shyam, d_shyam);



	}
	return 0;
}