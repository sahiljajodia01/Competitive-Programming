// O(n) solution using stacks

#include <bits/stdc++.h>

using namespace std;


void showstack(stack <int> s) 
{ 
    while (!s.empty()) 
    { 
        cout << '\t' << s.top(); 
        s.pop(); 
    } 
    cout << '\n'; 
} 


int main() {
    int n;
    cin >> n;
    while(n != 0) {
        vector<int> v(n);

        for(int i = 0; i < n; i++) {
            cin >> v[i];
        }

        stack<int> st;
        vector<int> sol;
        // int min_ele = *min_element(v.begin(), v.end());
        int flag = 0;
        for(int i = 0; i < n; i++) {
            while(!st.empty()) {
                if(sol.size() > 0) {
                    if(st.top() == sol.back() + 1) {
                        sol.push_back(st.top());
                        st.pop();
                    }
                    else {
                        break;
                    }
                }
                else {
                    break;
                }
            }
            
            

            if(sol.size() > 0) {
                // cout << "Inside if" << "\n";
                if(v[i] == sol.back() + 1) {
                    sol.push_back(v[i]);
                }
                else {
                    if(st.empty()) {
                        st.push(v[i]);
                    }
                    else {
                        if(v[i] < st.top()) {
                            st.push(v[i]);
                        }
                        else {
                            flag = 1;
                            break;
                        }
                    }
                    
                }
            }
            else {
                // cout << "Inside else" << "\n";
                if(v[i] == 1) {
                    sol.push_back(v[i]);
                }
                else {
                    st.push(v[i]);
                }
            }

            // cout << "Sol: " << "\n";
            // for(int j = 0; j < sol.size(); j++) {
            //     cout << sol[j] << " ";
            // }
            // cout << "\n";


            // cout << "Stack: " << "\n";
            // showstack(st);
            // cout << "\n";

            // while(!st.empty() && st.top() == sol.back() + 1) {
            //     int temp = st.top();
            //     st.pop();
            //     sol.push_back(temp);
            // }
        }


        while(!st.empty()) {
            if(st.top() == sol.back() + 1) {
                sol.push_back(st.top());
                st.pop();
            }
            else {
                flag = 1;
                break;
            }
        }

        for(int i = 1; i < sol.size(); i++) {
            if(sol[i] != sol[i-1] + 1) {
                flag = 1;
                break;
            }
        }

        if(flag == 0) {
            cout << "yes" << "\n";
        }
        else {
            cout << "no" << "\n";
        }

        cin >> n;
    }
    

    return 0;
}