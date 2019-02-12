// 1114A

#include <bits/stdc++.h>

using namespace std;

int main() {
    int x, y, z;
    int a, b, c;

    cin >> x >> y >> z;
    cin >> a >> b >> c;

    int flag1 = 0, flag2 = 0, flag3 = 0;

    if(a - x >= 0) {
        flag1 = 1;
        a -= x;
    }
    // cout << "A: " << a << "\n";
    if((a + b - y) >= 0) {
        flag2 = 1;
        while(a > 0 && y > 0) {
            a--;
            y--;
            // cout << "A: " << a << "\n";
        }
        b -= y;
    }

    // cout << "A: " << a << "\n";
    // cout << "B: " << b << "\n";

    if((a + b + c - z) >= 0) {
        flag3 = 1;
    }

    if(flag1 == 1 && flag2 == 1 && flag3 == 1) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }

    return 0;
}