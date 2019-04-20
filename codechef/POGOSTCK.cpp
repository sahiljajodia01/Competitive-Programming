#include <bits/stdc++.h>

using namespace std;

void pogo_stick(vector<int> v, int k) {
    int sum = 0;
    for(int i = 0; i < v.size(); i++) {
        int temp = 0;
        for(int j = i; j < v.size(); j += k) {
            temp += v[j];
        }

        if(temp > sum) {
            sum = temp;
        }
    }

    cout << sum << "\n";
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