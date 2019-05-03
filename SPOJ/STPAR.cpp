#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v(n);

    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }

    stack<int> st;
    vector<int> sol;
    int min_ele = *min_element(v.begin(), v.end());
    int flag = 0;
    for(int i = 0; i < n; i++) {
        if(i == 0) {
            if(v[i] == 1)
                sol.push_back(v[i]);
            else
                st.push(v[i]);
        }
        else {
            if(sol.size() == 0) {
                if(v[i] == 1)
                    sol.push_back(v[i]);
            }
            else if(sol.size() != 0) {
                if(v[i] == sol.back() + 1) {
                    sol.push_back(v[i]);
                }
            }
            else {
                if(st.top() > v[i]) {
                    st.push(v[i]);
                }
                else{
                    flag = 1;
                }
            }
            
        }

        while(!st.empty() && st.top() == sol.back() +1) {
            int temp =  st.top();
            sol.push_back(temp);
            st.pop();
        }
        
    }

    for(int i = 1; i < sol.size(); i++) {
        if(v[i] != v[i-1] + 1){
            flag = 1;
        }
    }

    if(flag == 0) {
        cout << "yes" << "\n";
    }
    else {
        cout << "no" << "\n";
    }

    return 0;
}