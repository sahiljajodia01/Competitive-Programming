#include <bits/stdc++.h>

using namespace std;

int distinct_occurences(int x, int y, string a, string b) {
    int sum = 0;
    // if(y == 0 && (a[x] == b[y])) {
    //     return 1;
    // }
    // else if(x == 0 || (a[x] != b[y])) {
    //     return 0;
    // }

    if(y == 0 && x >= 0) {
        if(a[x] == b[y]) {
            return 1;
        }
    }
    else if(x == 0 && y > 0) {
        return 0;
    }

    if(a[x] == b[y]) {
        sum += distinct_occurences(x-1, y-1, a, b);
    }
    else {
        sum += distinct_occurences(x-1, y, a, b);
        sum += distinct_occurences(x, y-1, a, b);
    }
    return sum;

}

int main() {
    int t;
    cin >> t;

    while(t--) {
        string a, b;

        cin >> a >> b;

        int ans =  distinct_occurences(a.length()-1, b.length()-1, a, b);

        cout << ans << "\n";
    }


    return 0;
}