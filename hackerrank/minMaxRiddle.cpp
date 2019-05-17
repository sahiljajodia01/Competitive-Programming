
// O(n^3) Brute force approach. Accepted only for 30 points.
// A O(n^2) aproach using tables and O(n) approach using stacks is also available.
// Also a divide and conquer approach is mentioned in the discussions.

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n);

    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }

    vector<int> sol;
    for(int i = 0; i < n; i++) {
        vector<int> max;
        for(int j = 0; j < n - i; j++) {
            int m = v[j];
            for(int k = j; k < j + i + 1; k++) {
                if (v[k] < m) {
                    m = v[k];
                }
            }
            max.push_back(m);
        }
        int maximum = *max_element(max.begin(), max.end());
        sol.push_back(maximum);
    }

    // cout << "Solution: " << '\n';

    for(int i = 0; i < sol.size(); i++) {
        cout << sol[i] << " ";
    }
    cout << "\n";

    return 0;
}