#include <bits/stdc++.h>

using namespace std;

bool isPerfectSquare(long double x) 
{   
  long double sr = sqrt(x); 
  
  return ((sr - floor(sr)) == 0); 
} 

int main() {
    int t;

    cin >> t;

    while(t--) {
        long double n;

        cin >> n;
        long double copy = n;
        int count = 0;
        long double diff = copy;
        while(diff > 0) {
            copy = n;
            while(!isPerfectSquare(copy)) {
                copy--;
            }

            diff = n - copy;
            n = diff;
            if(copy > 0) {
                count++;
            }
        }


        cout << count << "\n";
    


        
    }
    return 0;
}