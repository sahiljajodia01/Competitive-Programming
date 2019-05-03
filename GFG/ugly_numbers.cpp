// https://www.geeksforgeeks.org/ugly-numbers/

// Complexity is O(n) after using dynamic programming

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> dp;
    dp.push_back(0);
    dp.push_back(1);
    int count = 2;
    vector<int> sol(n);
    sol[0] = 1;
    int c = 1;
    while(c < n) {
        while(true) {
            if(count%2 == 0) {
                if(dp[count/2] == 1) {
                    dp.push_back(1);
                    break;
                }
                else {
                    dp.push_back(0);
                }
            }
            else {
                if(count % 3 == 0) {
                    if(dp[count/3] == 1) {
                        dp.push_back(1);
                        break;
                    }
                    else {
                        dp.push_back(0);
                    }
                }
                else if(count % 5 == 0) {
                    if(dp[count/5] == 1) {
                        dp.push_back(1);
                        break;
                    }
                    else {
                        dp.push_back(0);
                    }
                }
                else {
                    dp.push_back(0);
                }
            }
            count++;
        }
        sol[c] = count;
        c++;
        count++;
    }

    cout << sol[n-1] << "\n";

}