#include <bits/stdc++.h>

using namespace std;

///////////////////// This solution gives TLE //////////////////////////

// void min_time(vector<int> v, int g) {
// 	long count = g;
// 	long days = 0;
// 	while(true) {
// 	// 	long minus = 0;
// 	// 	days++;
// 		// for(long i = 0; i < v.size(); i++) {
// 		// 	minus += (long)days/v[i];
// 		// 	cout << "Minus: " << minus << "\n";
// 		// }

// 	// 	count -= minus;
// 	// 	cout << "Count: " << count << "\n";
// 	// }
// 	// cout << days << "\n";
// 		days++;
// 		long minus = 0;
// 		for(long i = 0; i < v.size(); i++) {
// 			minus += (long)days/v[i];
// 			// cout << "Minus: " << minus << "\n";
// 		}
// 		if(minus >= count) {
// 			break;
// 		}
// 	}
// 	cout << days << "\n";

// }


//////////////////// A different solution using binary search /////////////////////

int get_units(int day, vector<int> v, int g) {
	int units = 0;
	for(int i = 0; i < v.size(); i++) {
		units += day/v[i];
	}
	return units;
}


void min_time(vector<int> v, int g) {
	long max = *max_element(v.begin(), v.end());
	long min = *min_element(v.begin(), v.end());

	cout << "Max: " << max << "\n";
	cout << "Min: " << min << "\n";
	long ratio = (long)ceil((float)g/v.size());
	cout << "Ratio: " << ratio << "\n";

	long min_days = min*ratio;
	long max_days = max*ratio;

	cout << "Min days: " << min_days << "\n";
	cout << "Max days: " << max_days << "\n";

	while(min_days < max_days) {
		long days = (min_days + max_days)/2;
		long units = get_units(days, v, g);
		cout << "Units: " << units << " | Days: " << days << "\n";
		if(units >= g) {
			max_days = days;
		}
		else if(units < g) {
			min_days = days + 1;
		}
	}
	// cout << min_days << "\n";
	return min_days;
}



int main() {
	int n, goal;
	vector<int> v;

	cin >> n >> goal;

	for(int i = 0; i < n; i++) {
		int temp;
		cin >> temp;

		v.push_back(temp);
	}

	min_time(v, goal);

	return 0;
}