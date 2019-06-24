#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;

    cin >> t;

    while(t--) {
        int r, c;

        cin >> r >> c;

        vector< vector<int> > v(r);

        for(int i = 0; i < r; i++) {
            vector<int> temp(c);
            for(int j = 0;j < c; j++) {
                cin >> temp[j];
            }
            v[i] = temp;
        }
        int flag = 0;
        for(int i = 0; i < r; i++) {
            vector<int> temp = v[i];
            for(int j = 0; j < c; j++) {
                if(i % (v.size()-1) == 0 && j % (temp.size()-1) == 0) {
                    if(2 > v[i][j]) {
                        continue;
                    }
                    else {
                        flag = 1;
                        break;
                    }
                }
                else if(i % (v.size()-1) == 0 && j % (temp.size()-1) != 0) {
                    if(3 > v[i][j]) {
                        continue;
                    }
                    else {
                        flag = 1;
                        break;
                    }
                }
                else if(i % (v.size()-1) != 0 && j % (temp.size()-1) == 0) {
                    if(3 > v[i][j]) {
                        continue;
                    }
                    else {
                        flag = 1;
                        break;
                    }
                }
                else if(i % (v.size()-1) != 0 && j % (temp.size()-1) != 0) {
                    if(4 > v[i][j]) {
                        continue;
                    }
                    else {
                        flag = 1;
                        break;
                    }
                }
                
            }
        }

        if(flag == 0) {
            cout << "Stable" << "\n";
        }
        else {
            cout << "Unstable" << "\n";
        }
    }

    return 0;
}