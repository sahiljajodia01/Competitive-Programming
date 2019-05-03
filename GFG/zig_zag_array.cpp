#include <bits/stdc++.h>

using namespace std;

void zig_zag(vector<int> v) {
    sort(v.begin(), v.end());

    vector<int> sol(v.size());

    int counter = 0;
    for(int i = 0; i < v.size(); i += 2) {
        sol[i] = v[counter];
        counter++;
    }

    for(int i = 1; i < v.size(); i += 2) {
        sol[i] = v[counter];
        counter++;
    }

    cout << "Final arr: " << "\n";

    for(int i = 0; i < sol.size(); i++) {
        cout << sol[i] << " ";
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        vector<int> v(n);
        
        for(int i = 0; i < n; i++) {
            cin >> v[i];
        }

        zig_zag(v);
    }

    return 0;
}