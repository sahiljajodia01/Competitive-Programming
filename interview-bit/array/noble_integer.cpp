#include <bits/stdc++.h>

using namespace std;

void noble_integer(vector<int> &A) {

    ////////////// MEMORY INEFFICENT BUT TIME EFFICIENT(N) WHICH DOES NOT PASS ON INTERVIEW BIT /////////////////
    // map<int, int> m;

    // for(int i = 0; i < A.size(); i++) {
    //     if(m.find(A[i]) == m.end()) {
    //         m[A[i]] = 1;
    //     }
    //     else {
    //         m[A[i]]++;
    //     }
    // }

    // int count = 1;
    // int m_size = 0;
    // int flag = 0;

    // // cout << "Map is: " << "\n";
    // for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
    //     int first = it->first;
    //     int second = it->second;

    //     m_size += second;
    //     // cout << first << "-" << second << "\n";
    // }
    // for(map<int, int>::iterator it = m.begin(); it != m.end(); it++) {
    //     int first = it->first;
    //     int second = it->second;

    //     m_size -= second;
    //     if(first == m_size) {
    //         // cout << "Integer P: " << first << "\n";
    //         flag = 1;
    //         break;
    //     }
    //     // count++;
    // }



    /////////// MEMORY EFFICIENT SOLUTION WHICH PASSES ON INTERVIEW BIT BUT LESS TIME EFFICIENT(NLOG(N)) THAN ABOVE SOLUTION ////////////
    sort(A.begin(), A.end());
    cout << "Sorted arr: " << "\n";
    for(int i = 0; i < A.size(); i++) {
        cout << A[i] << "\t";
    }
    cout << "\n";
    int s = A.size();
    int flag = 0;
    for(int i = 0; i < A.size(); i++) {
        s--;
        int count = 0;
        if(A[i] == s) {
            if(i != A.size() - 1) {
                if(A[i+1] > A[i]) {
                    flag = 1;
                    break;
                }
            }
            else{
                flag = 1;
                break;
            }
        }
    }



    if(flag == 0) {
        cout << -1 << "\n";
        // return -1;
    }
    else {
        cout << 1 << "\n";
        // return 1;
    }
}

int main() {
    // int t;

    // cin >> t;

    // while(t--) {
        // int n;

        // cin >> n;
    int arr[] = {-4, -2, 0, -1, -6};
    // int arr[] = { -4, 7, 5, 3, 5, -4, 2, -1, -9, -8, -3, 0, 9, -7, -4, -10, -4, 2, 6, 1, -2, -3, -1, -8, 0, -8, -7, -3, 5, -1, -8, -8, 8, -1, -3, 3, 6, 1, -8, -1, 3, -9, 9, -6, 7, 8, -6, 5, 0, 3, -4, 1, -10, 6, 3, -8, 0, 6, -9, -5, -5, -6, -3, 6, -5, -4, -1, 3, 7, -6, 5, -8, -5, 4, -3, 4, -6, -7, 0, -3, -2, 6, 8, -2, -6, -7, 1, 4, 9, 2, -10, 6, -2, 9, 2, -4, -4, 4, 9, 5, 0, 4, 8, -3, -9, 7, -8, 7, 2, 2, 6, -9, -10, -4, -9, -5, -1, -6, 9, -10, -1, 1, 7, 7, 1, -9, 5, -1, -3, -3, 6, 7, 3, -4, -5, -4, -7, 9, -6, -2, 1, 2, -1, -7, 9, 0, -2, -2, 5, -10, -1, 6, -7, 8, -5, -4, 1, -9, 5, 9, -2, -6, -2, -9, 0, 3, -10, 4, -6, -6, 4, -3, 6, -7, 1, -3, -5, 9, 6, 2, 1, 7, -2, 5 };
    int n = sizeof(arr) / sizeof(arr[0]); 
    vector<int> a(arr, arr + n); 
        // for(int i = 0; i < n; i++) {
        //     cin >> a[i];
        // }

    noble_integer(a);
    // }
    return 0;
}