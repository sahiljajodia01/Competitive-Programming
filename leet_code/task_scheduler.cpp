// https://leetcode.com/submissions/detail/226325670/


// This code not working. Refer to python code of the same problem for the working code.
#include <bits/stdc++.h>

using namespace std;

int main() {
    map<char, int> m;
    int n, k;
    cin >> n >> k;
    vector<char> sol;
    while(n--) {
        char temp;
        cin >> temp;
        // v.push_back(temp);
        if(m.find(temp) == m.end()) {
            m[temp] = 1;
        }
        else {
            m[temp]++;
        }
    }
    k = k - m.size() + 1;
    while(true) {
        for(map<char, int>::iterator it = m.begin(); it != m.end(); it++) {
            char first = it->first;
            char second = it->second;
            if(second > 0){
                sol.push_back(first);
                m[first]--;
            }

            int flag1 = 0;
            for(map<char, int>::iterator it1 = m.begin(); it1 != m.end(); it1++) {
                int second1 = it1->second;

                if(second1 > 0) {
                    flag1 = 1;
                    break;
                }
            }

            if(flag1 != 0) {
                if(second == 0) {
                    sol.push_back(',');
                }
            }

            
        }

        int flag = 0;
        for(map<char, int>::iterator it = m.begin(); it != m.end(); it++) {
            int second = it->second;

            if(second > 0) {
                flag = 1;
                break;
            }
        }

        if(flag == 0) {
            break;
        }

        for(int i = 0; i < k; i++) {
            sol.push_back(',');
        }
    }

    cout << "Sol: " << "\n";
    for(int i = 0; i < sol.size(); i++) {
        cout << sol[i] << " ";
    }
    cout << "\n";

    cout << sol.size() << "\n";

    


    return 0;
}