#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;

    cin >> t;

    while(t--) {
        int n, b;

        cin >> n >> b;
        int area = 0;

        for(int i = 0; i < n; i++) {
            int a, f, c;
            cin >> a >> f >> c;
            if(c <= b) {
                int temp = a*f;
                if(temp > area) {
                    area = temp;
                }
            }
        }

        if(area == 0) {
            cout << "no tablet" << "\n";
        }
        else {
            cout << area << "\n";
        }
    }


    return 0;
}