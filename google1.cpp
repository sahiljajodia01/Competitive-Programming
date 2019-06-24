#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;

    cin >> t;

    for(int z = 1; z <= t; z++) {
        int x;
        cin >> x;
        int n;
        vector<int> v;
        cin >> n;

        for(int i = 0; i < n; i++) {
            string t;
            int h;
            cin >> t >> h;

            v.push_back(h);
        }


        int m;
        vector<int> v1;
        cin >> m;

        for(int i = 0; i < m; i++) {
            string t;
            int h;
            cin >> t >> h;

            v1.push_back(h);
        }

        vector<int> prices;
        int flag1 = 0, flag2 = 0;
        int max = v[0];
        for(int i = 0; i < v.size(); i++) {
            prices.push_back(v[i]);
            for(int j = 0; j < v1.size(); j++) {
                int sum = v[i] + v1[j];
                prices.push_back(sum);
            }

            if(flag1 == 0) {
                for(int j = 0; j < v1.size(); j++) {
                    for(int k = j+1; k < v1.size(); k++) {
                        int sum = v[i] + v1[j] + v1[k];
                        prices.push_back(sum);
                    }
                }
            }
        }

        vector<int> diff;

        for(int i = 0; i < prices.size(); i++) {
            int d = x - prices[i];

            diff.push_back(d);
        }

        int minimum = INT_MAX;
        for(int i = 0; i < diff.size(); i++) {
            if(abs(diff[i]) < minimum) {
                minimum = abs(diff[i]);
            }
        }
        vector<int> indexes;
        for(int i = 0; i < diff.size(); i++) {
            if(abs(diff[i]) == minimum) {
                indexes.push_back(i);
            }
        }

        int min = INT_MAX;
        for(int i = 0; i < indexes.size(); i++) {
            if(prices[indexes[i]] < min) {
                min = prices[indexes[i]];
            }
        }

        cout << "Case #" << z << ": " << min << "\n";
    }
    return 0;
}