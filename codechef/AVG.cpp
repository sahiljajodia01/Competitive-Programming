#include <bits/stdc++.h>

using namespace std;

void avg(vector<int> vec, int k, int v) {
    int tot = (vec.size() + k) * v;

    for(int i = 0; i < vec.size(); i++) {
        tot -= vec[i];
        // cout << "tot: " << tot << "\n";
    }

    if(tot <= 0 || tot % k != 0) {
        cout << -1 << "\n";
    }
    else {
        cout << tot/k << "\n";
    }
}

int main() {
    int t;

    cin >> t;

    while(t--) {
        int n, k, v;

        cin >> n >> k >> v;
        vector<int> vec(n);

        for(int i = 0; i < n; i++) {
            cin >> vec[i];
        }


        avg(vec, k, v);
    }

    return 0;
}