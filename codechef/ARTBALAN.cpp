#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

vector<ll> factors(ll s) {
	ll temp = 1;
	vector<ll> v;
	while(temp <= s) {
		if(s % temp == 0)
			v.push_back(temp);
		temp++;
	}
	return v;
}


void art_balance(string s) {
	// cout << "Inside func" << "\n";
	map<char, ll> m;

	for(ll i = 0; i < s.length(); i++) {
		if(m.find(s[i]) == m.end()) {
			m[s[i]] = 1;
		}
		else {
			m[s[i]]++;
		}
	}

	// cout << "Map: " << "\n";
	// for(map<char, ll>::iterator it = m.begin(); it != m.end(); it++) {
	// 	cout << it->first << " - " << it->second << "\n";
	// }
	// cout << "After for" << "\n";
	// map<int, int> map_of_values;

	// for(map<char, int>::iterator it = m.begin(); it != m.end(); it++) {
	// 	int second = it->second;

	// 	if(map_of_values.find(second) == map_of_values.end()) {
	// 		map_of_values[second] = 1;
	// 	}
	// 	else {
	// 		map_of_values[second]++;
	// 	}
	// }

	// int count = 0;
	// if(map_of_values.size() == 1) {
	// 	cout << 0 << "\n";
	// }
	// else {
	// 	vector<int> v = factors(s.length());
	// 	int min = INT_MAX;
	// 	for(int i = 0 i < v.size(); i++) {
	// 		int count = 0;
	// 		int value = v[i];
	// 		while(true) {
	// 			for(map<int, int>::reverse_iterator it = m.rbegin(); it != m.rend(); ++it) {
	// 				int first = it->first;
	// 				int second = it->second;
	// 				int x = abs(value - first);

	// 				if(x == 0)
	// 					continue;

	// 				if(map_of_values.find(x) != map_of_values.end())
	// 				{
	// 					if(x)
	// 					map_of_values[value] = 1;
	// 					map_of_values[x]->second--;
	// 				}
	// 			}
	// 		}
			
	// 	}
	// }

	vector<ll> v = factors(s.length());
	// cout << "Factors: " << "\n";
	// for(int i = 0; i < v.size(); i++) {
	// 	cout << v[i] << " ";
	// }
	// cout << "\n";
	ll min = LONG_LONG_MAX;
	// cout << "Before for" << "\n";
	for(ll i = 0; i < v.size(); i++) {

		// if(s.length() > 26 && v.size() == 2) {
		// 	if(v[i] != v[1])
		// 		continue;
		// }
		// cout << "Inside for" << "\n";
		ll count = 0;
		ll value = v[i];
		ll cou = s.length()/v[i];

		if(cou > 26)
			continue;

		vector<ll> diff(m.size());
		// vector<int> orig(m.size());
		ll c = 0;

		for(map<char, ll>::iterator it = m.begin(); it != m.end(); it++) {
			ll second = it->second;

			diff[c] = value - second;
			c++;
		}

		sort(diff.begin(), diff.end());

		// cout << "Diff Array: " << "\n";
		// for(int i = 0; i < diff.size(); i++) {
		// 	cout << diff[i] << "\n";
		// }
		// cout << "\n";
		// sort(copy.begin(), copy.end());

		// if(diff.size() > cou) {
			// cout << "Inside if" << "\n"; 
		for(ll i = diff.size() - 1; i >= cou; i--) {
			// cout << "Inside for" << "\n";
			// cout << "DIFF : " << diff[i];
			count += (value - diff[i]);
		}

		for(ll i = 0; i < diff.size(); i++) {
			if(diff[i] < 0) {
				count += diff[i]*-1;
			}
			else {
				break;
			}
		}
		// }
		// else {
			// cout << "Inside else" << "\n";
		// 	for(ll i = 0; i < diff.size(); i++) {
		// 		if(diff[i] < 0)
		// 			count += abs(diff[i]);
		// 		else
		// 			break;
		// 	}
		// }
		// cout << "Count for value = " << value << " is " << count << "\n";

		if(count < min) {
			min = count;
		}
	}

	cout << min << "\n";


}

int main() {
	ll t;

	cin >> t;

	while(t--) {
		string s;
		cin >> s;

		art_balance(s);
	}
}