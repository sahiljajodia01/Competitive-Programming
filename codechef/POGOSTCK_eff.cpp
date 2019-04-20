#include <bits/stdc++.h>

using namespace std;

void pogo_stick(vector<int> v, int k) {

    if(k > v.size()) {
        int max = *max_element(v.begin(), v.end());
        cout << max << "\n";
    }
    else {
        // int sum = 0;
        // for(int i = v.size() - 1; i >= v.size() - k; i--) {
        //     // cout << "For i = " << i << "\n";
        //     int temp = 0;
        //     for(int j = i; j >= 0; j -= k) {
        //         temp += v[j];
        //         // cout << "Temp: " << temp << "\n";
        //         if(temp > sum) {
        //             sum = temp;
        //         }
        //     }
        // }

        for(int i = v.size() - k - 1; i >= 0; i--) {
            v[i] += v[i+k];
        }

        // cout << "array: " << "\n";
        // for(int i = 0; i < v.size(); i++) {
        //     cout << v[i] << " ";
        // }
        // cout << "\n";

        int max = *max_element(v.begin(), v.end());

        cout << max << "\n";
        // cout << sum << "\n";
    }
}

int main() {
    int t;

    cin >> t;

    while(t--) {
        int n, k;

        cin >> n >> k;

        vector<int> v(n);

        for(int i = 0; i < n; i++) {
            cin >> v[i];
        }

        pogo_stick(v, k);
    }

    return 0;
}