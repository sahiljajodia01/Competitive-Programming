#include <bits/stdc++.h>

using namespace std;

void palindrome(int n, int copy, int sum) {
    int temp = 0;

    if(n == 0) {
        if(sum == copy) {
            cout << "Palindrome!" << "\n";
        }
        else {
            cout << "Not Palindrome!" << "\n";
        }
        return;
    }
    else {
        temp = n%10;
        // cout << "Temp: " << temp << "\n";
        sum = sum*10 + temp;
        // cout << sum << "\n";
        return palindrome(n/10, copy, sum);
    }

}

int main() {
    int n;

    cout << "Enter a number: ";
    cin >> n;

    palindrome(n, n, 0);

    return 0;
}