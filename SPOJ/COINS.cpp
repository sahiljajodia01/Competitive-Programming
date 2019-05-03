#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;

    cin >> n;

    vector<int> v(n+1, 0);

    for(int i = 0; i < v.size(); i++) {
        int temp = v[i/2] + v[i/3] + v[i/4];
        cout << "Temp: " << temp << "\n";

        if(temp > i) {
            v[i] = temp;
        }
        else {
            v[i] = i;
        }
    }

    cout << "V: " << "\n";
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << "\n";

    cout << "Final ans: " << v[n] << "\n";

    return 0;
}