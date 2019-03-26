#include <bits/stdc++.h>

using namespace std;

int contains_three(int n) {
    int count = 0;
    while(n != 0) {
        int temp = n % 10;
        if(temp == 3) {
            count++;
        }
        n = n/10;
    }
    return count;
}

void bftt(int n) {
    int ans;
    for(int i = n+1; i < n + 1000; i++) {
        int count = contains_three(i);

        if(count == 3) {
            ans = i;
            break;
        }
    }

    cout << ans << "\n";

    
}

int main(){
    int t;

    cin >> t;

    while(t--) {
        int n;

        cin >> n;

        bftt(n);
    }


    return 0;
}