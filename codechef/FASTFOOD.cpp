#include <bits/stdc++.h>

using namespace std;


// Complexity O(n^2) Works only partially!
// void fastfood(vector<int> a, vector<int> b) {
//     int sum = 0;
    
//     for(int i = 0; i < b.size(); i++) {
//         sum += b[i];
//     }

//     for (int i = 0; i < a.size(); i++) {
//         int total = 0;
//         for(int j = 0; j <= i; j++) {
//             total += a[j];
//         }

//         for(int j = i+1; j < b.size(); j++) {
//             total += b[j];
//         }
//         // cout << "Total: " << total << "\n";
//         if(total > sum) {
//             sum = total;
//         }
//     }

//     cout << sum << "\n";

// }



// Still NOT COMPLETED. I have to commit this
void fastfood(vector<int> a, vector<int> b) {
    for(int i = 1; i < a.size(); i++) {
        a[i] = a[i] + a[i-1];
        b[i] = b[i] + b[i-1];
    }

    cout << "Print A: " << "\n";
    for(int i = 0; i < a.size(); i++) {
        cout << a[i] << " ";
    }
    cout << "\n";

    cout << "Print B: " << "\n";
    for(int i = 0; i < b.size(); i++) {
        cout << b[i] << " ";
    }
    cout << "\n";

    int flag = 0;
    int sum = 0
    int i = 0;
    for(i = 0; i < a.size(); i++) {
        if(b[i] >= a[i]) {
            flag = 1;
            break;
        }
    }

    for(int j = 0; j < i; j++) {

    }

}



int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;

        vector<int> a(n), b(n);

        for(int i = 0; i < n; i++) {
            cin >> a[i];
        }

        for(int i = 0; i < n; i++) {
            cin >> b[i];
        }

        fastfood(a, b);
    }

    return 0;
}