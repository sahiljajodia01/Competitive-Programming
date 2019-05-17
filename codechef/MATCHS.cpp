#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll n, m;

        cin >> n >> m;

        ll count = 0, ari = 0, rich = 0;


        while(n != 0 && m != 0) {
            // ll max = n > m ? n : m;

            if(count % 2 == 0) {
                ari++;
                if(n > m) {
                    // cout << "Inside if" << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                    // ll fact = n/m;

                    // if(n % m != 0) {
                    //     if(fact != 1) {
                    //         if(fact % 2 == 0) {
                    //             n -= m*fact;
                    //         }
                    //         else {
                    //             n -= m*(fact-1);
                    //         }
                    //     }
                    //     else {
                    //         n -= m*fact;
                    //     }
                    // }
                    // else {
                    //     n -= m*fact;
                    // }
                    n = n % m;

                    // cout << "Fact: " << fact << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                }
                else {
                    // cout << "Inside else" << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                    // ll fact = m/n;

                    // if(m % n != 0) {
                    //     if(fact != 1) {
                    //         if(fact % 2 == 0) {
                    //             m -= n*fact;
                    //         }
                    //         else {
                    //             m -= n*(fact-1);
                    //         }
                    //     }
                    //     else {
                    //         m -= n*fact;
                    //     }
                    // }
                    // else {
                    //     m -= n*fact;
                    // }

                    m = m % n;
                    // cout << "Fact: " << fact << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                }
            }
            else {
                rich++;
                if(n > m) {
                    // cout << "Inside 2nd if" << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                    // ll fact = n/m;

                    // if(n % m != 0) {
                    //     if(fact != 1) {
                    //         if(fact % 2 == 0) {
                    //             n -= m*fact;
                    //         }
                    //         else {
                    //             n -= m*(fact-1);
                    //         }
                    //     }
                    //     else {
                    //         n -= m*fact;
                    //     }
                    // }
                    // else {
                    //     n -= m*fact;
                    // }

                    n = n % m;
                    // n -= m*fact;
                    // cout << "Fact: " << fact << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                }
                else {
                    // cout << "Inside 2nd else" << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                    ll fact = m/n;

                    // if(m % n != 0) {
                    //     if(fact != 1) {
                    //         if(fact % 2 == 0) {
                    //             m -= n*fact;
                    //         }
                    //         else {
                    //             m -= n*(fact-1);
                    //         }
                    //     }
                    //     else {
                    //         m -= n*fact;
                    //     }
                    // }
                    // else {
                    //     m -= n*fact;
                    // }

                    m = m % n;

                    // m -= n*fact;
                    // cout << "Fact: " << fact << "\n";
                    // cout << "n: " << n << " m: " << m << "\n";
                }
            }
            // cout << "Ari: " << ari << " Rich: " << rich << "\n";
            count++;
        }

        if(ari > rich) {
            cout << "Ari" << "\n";
        }
        else {
            cout << "Rich" << "\n";
        }
    }

    return 0;
}