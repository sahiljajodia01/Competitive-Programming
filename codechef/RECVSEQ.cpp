// Not completed fully

#include <bits/stdc++.h>

using namespace std;

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
        // int diff = v[1] - v[0];
        // int diff1 = v[2] - v[1];
        // int diff2 = v[3] - v[2];
        // int flag = 0;
        // if(diff == diff1 && diff1 == diff2) {
        //     flag = 1;
        // }
        // else if( diff == diff1 && diff1 != diff2) {
            
        // }

        vector<int> diff;

        for(int i = 1; i < v.size(); i++) {
            int di = v[i] - v[i-1];
            diff.push_back(di);
        }

        map<int, int> m;
        for(int i = 0; i < diff.size(); i++) {
            if(m.find(diff[i]) == m.end()) {
                m[diff[i]] = 1;
            }
            else {
                m[diff[i]]++;
            }
        }
        int max = m.begin()->second;
        int max_ele = m.begin()->first;
        if(m.size() == 1) {
            for(int i = 0; i < v.size(); i++) {
                cout << v[i] << " ";
            }
            cout << "\n";
        }
        else {
            for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
                int second = it->second;
                int first = it->first;

                if(max > second) {
                    max = second;
                    max_ele = first;
                }
            }

            cout << "Max_ele: " << max_ele << "\n";

            vector<int> index;

            for(int i = 0; i < diff.size(); i++) {
                if(v[i] != max_ele) {
                    index.push_back(i);
                }
            }
            if(index.size() == 1) {
                int ele;
                if(index[0] == 0) {
                    if(diff[0] > max_ele) {
                        ele = v[0] + diff[0] - max_ele;
                    }
                    else {
                        ele = v[0] + diff[0] - max_ele;
                    }
                }

                cout << ele << " ";
                for(int i = 1; i < v.size(); i++) {
                    cout << ele + i*max_ele << " ";
                }
                cout << "\n";
            }
            else {
                cout << v[0] << " ";
                for(int i = 1; i < v.size(); i++) {
                    cout << v[0] + i*max_ele << " ";
                }
                cout << "\n";
            }
        //     for(int i = 0; i < index.size(); i++) {
        //         int h = diff[i];
        //     }
        // }
        // // int second_max = max;
    
        // for(int i = 0; i < v.size(); i++) {

        // }
        
        }
    }
    return 0;
}