// Showing runtime(SIGABART) error for this solution


#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;

ll binaryToDecimal(ll n) 
{ 
    ll num = n; 
    ll dec_value = 0; 
      
    // Initializing base value to 1, i.e 2^0 
    ll base = 1; 
      
    ll temp = num; 
    while (temp) 
    { 
        ll last_digit = temp % 10; 
        temp = temp/10; 
          
        dec_value += last_digit*base; 
          
        base = base*2; 
    } 
      
    return dec_value; 
} 

void binary_strings(string s) {
    ll count = 0;
    for(ll i = 0; i < s.length(); i++) {
        char c = s[s.length() - 1];

        for(ll j = s.length() - 1; j >= 1; j--) {
            s[j] = s[j - 1];
        }
        s[0] = c;


        ll num = stoi(s);
        ll dec_num = binaryToDecimal(num);

        if(dec_num % 2 != 0) {
            count++;
        }
    }

    cout << count << "\n";
}



int main() {
    ll t;

    cin >> t;

    while(t--) {
        ll n;
        cin >> n;
        string s;

        cin >> s;

        binary_strings(s);
    }
    return 0;
}