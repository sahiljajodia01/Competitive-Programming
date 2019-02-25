#include <bits/stdc++.h>

using namespace std;



void party(vector<int> v) {
    int count = 0;;
    sort(v.begin(), v.end());
    for(int i = 0; i < v.size(); i++) {
        if(v[i] <= count) {
            count++;
        }
    }

    cout << count << "\n";
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

        party(v);
    }


    return 0;
}