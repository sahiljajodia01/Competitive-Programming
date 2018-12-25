#include <bits/stdc++.h> 

using namespace std;




/////////////This solution is giving TLE ////////////////

// long special_palindrome(string s, int n) {
// 	long count = 0;
//     for(int i = 0; i < s.length(); i++) {
//         for(int j = 1; j <= s.length() - i; j++) {
//             int flag = 0;
//             string sub = s.substr(i, j);
//             // cout << "Sub: " << sub << "\n";
//             if(sub.length() == 1) {
//             	// cout << "First cond" << "\n";
//             }
//             else if(sub.length() % 2 == 0) {
//             	// cout << "Second cond" << "\n";
//                 char prev = sub[0];
//                 // cout << "Prev: " << prev << "\n";
//                 for(int k = 1; k < sub.length(); k++) {
//                     if(sub[k] == prev) {
//                         prev = sub[k];
//                     }
//                     else {
//                         // cout << "Wrong Sub: " << sub << "\n";
//                         flag = 1;
//                         break;
//                     }
//                 }
//             }
//             else {
//             	// cout << "Third cond" << "\n";
//                 char prev = sub[0];
//                 int mid = sub.length()/2;
//                 // cout << "Mid: " << mid << "\n";
//                 for(int k = 0; k < mid; k++) {
//                     if(sub[k] == prev) {
//                         prev = sub[k];
//                     }
//                     else {
//                         // cout << "Wrong Sub: " << sub << "\n";
//                         flag = 1;
//                         break;
//                     }
//                 }

//                 for(int k = mid+1; k < sub.length(); k++) {
//                     if(sub[k] == prev) {
//                         prev = sub[k];
//                     }
//                     else {
//                         // cout << "Wrong Sub: " << sub << "\n";
//                         flag = 1;
//                         break;
//                     }
//                 }
//             }
//             // cout << "Flag: " << flag << "\n";
//             if(flag == 0) {
//                 count++;
//             }
//         }
//     }

//     return count;
// }


////////////// Another solution using tuples! /////////////////

long special_palindrome(string s, int n) {
    // map<char, int> m;

    // for(int i = 0; i < n; i++) {
    // 	char c = s[i];
    // 	if(m.find(c) == m.end()) {
    // 		m[c] = 1;
    // 	}
    // 	else {
    // 		m[c]++;
    // 	}
    // }

    // map<char, int>::iterator it = m.begin();
	long total_cost = 0;
	int count  = 0;
    typedef vector< tuple <char, int> > vt;
    vt v;
    char prev = s[0];
    for(int i = 1; i < s.length(); i++) {
    	if(s[i] == prev) {
    		count++;
    	}
    	else {
    		v.push_back(make_tuple(s[i-1], count+1));
    		count = 0;
    		prev = s[i];
    	}
    }
    v.push_back(make_tuple(s[i-1, count+1]))


    char prev_c;
    int prev_t;
    char curr_c;
    int curr_t;
    char fut_c;
    int fut_t;

    tie(prev_c, prev_t) = v[0];
    total_cost = prev_t + prev_t - 1;

    for(int i = 1; i < v.size() - 1; i++) {
    	tie(curr_c, curr_t) = v[i];
    	tie(fut_c, fut_t) = v[i+1];
    	total_cost = curr_t + curr_t - 1;

    	if(curr_t == 1) {
    		if(prev_t == fut_t && prev_c == fut_c) {
    			total_cost = prev_t + prev_t - 1;
    		}
    	}

    	prev_c = curr_c;
    	prev_t = curr_c;
    }
    total_cost = fut_t + fut_t - 1;

    return total_cost;

}

int main() {
	int n;
	string s;

	cin >> n;
	cin >> s;
	long ans;

	ans = special_palindrome(s, n);
	cout << ans << "\n";

	return 0;
}