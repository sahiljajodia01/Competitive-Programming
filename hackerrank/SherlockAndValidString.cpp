#include <bits/stdc++.h>

using namespace std;


///////////////////////////////////////////////////////////////////////////////////////
//// This solution fails for only 4 test cases. The other solution to this problem is by using hashmaps.
//// But I was looking for some other solution to solve it. Hashmaps will be a de-facto solution for this problem.
///////////////////////////////////////////////////////////////////////////////////////

// int maxRepeating(vector<int> arr, int n, int k) 
// { 
//     // Iterate though input array, for every element 
//     // arr[i], increment arr[arr[i]%k] by k 
//     for (int i = 0; i< n; i++) 
//         arr[arr[i]%k] += k; 
  
//     // Find index of the maximum repeating element 
//     int max = arr[0], result = 0; 
//     for (int i = 1; i < n; i++) 
//     { 
//         if (arr[i] > max) 
//         { 
//             max = arr[i]; 
//             result = i; 
//         } 
//     } 
  
//     /* Uncomment this code to get the original array back 
//        for (int i = 0; i< n; i++) 
//           arr[i] = arr[i]%k; */
  
//     // Return index of the maximum element 
//     return result; 
// } 


// Complete the isValid function below.
string isValid(string s) {
    int flag = 0;
    vector<int> v;
    for(int i = 97; i <= 122; i++) {
        int count = 0;
        for(int j = 0; j < s.length(); j++) {
            if((char)i == (char)s[j]) {
                count++;
            }
        }
        if(count > 0) {
            v.push_back(count);
        }


        // if(count == 2 && flag == 0) {
        //     flag = 1;
        //     continue;
        // }
        // if(count >= 2 && flag == 1) {
        //     return "NO";
        // }
    }
    int min = 99999;
    for(int k = 0; k < v.size(); k++) {
        if(min > v[k]) {
            min = v[k];
        }
    }

    // int maxOccur = maxRepeating(v, v.size(), 99999);
    int sum = 0;
    for(int k = 0; k < v.size(); k++) {
        sum += v[k];
    }
    if(v.size() == 0) {
        return "NO";
    }
    float first = ((float)sum/v.size());
    cout << "First: " << first << "\n";
    float second = (float)(maxOccur + (float)1/v.size());
    cout << "Second: " << second << "\n";
    if(first > second) {
        return "NO";
    }
    else {
        return "YES";
    }
}

int main() {
    string s;
    cin >> s;
    string ans;
    ans = isValid(s);
    cout << ans << "\n";
    return 0;
}