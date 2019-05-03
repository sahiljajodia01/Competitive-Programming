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