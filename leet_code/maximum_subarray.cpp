#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v(n);

    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }

    vector< vector<int> > dp;
    for(int i = 0; i < n; i++) {
        vector<int> temp;

        for(int j = 0; j < n; j++) {
            temp.push_back(-1);
        }
        dp.push_back(temp);
    }

    for(int i = 0; i < n; i++) {
        dp[i][i] = v[i];
    }
    for(int i = 0; i < n; i++) {
        int temp = v[i];

        for(int j = i+1; j < n; j++) {
            dp[i][j] = dp[i][j-1] + v[j];
        }
    }
    
    int max = -1*INT_MAX;
    for(int i = 0; i < n; i++) {
        for(int j = i; j < n; j++) {
            if(dp[i][j] > max) {
                max = dp[i][j];
            }
        }
    }

    cout << "DP array: " << "\n";
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << dp[i][j] << " ";
        }
        cout << "\n";
    }


    cout << max << "\n";

    return 0;
}