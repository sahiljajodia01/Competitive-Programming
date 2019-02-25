#include <bits/stdc++.h>

using namespace std;

bool is_vowel(char c) {
    if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
        return true;
    }
    else {
        return false;
    }
}

void prob_chars(string s) {
    // if(!is_vowel(s[0]) || !is_vowel(s[s.length() - 1])){
    //     cout << 0 << "\n";
    //     return;
    // }
    vector<int> indexes;

    int count = 0;
    int start = 0;
    char prev = 'c';
    
    for(int i = 0; i < s.length(); i++) {
        if(prev == 'c' && is_vowel(s[i])) {
            prev = 'v';
            indexes.push_back(i);
        }
        else if(prev == 'v' && !is_vowel(s[i])) {
            prev = 'c';
        }
    }

    // cout << "Vowel Index list: " << "\n";
    // for(int i = 0; i < indexes.size(); i++) {
    //     cout << indexes[i] << " ";
    // }
    // cout << "\n";

    vector<int> string_sizes;
    if(!is_vowel(s[0]) && !is_vowel(s[s.length() - 1])) {
        // cout << "Inside 1st if" << "\n";
        for(int i = 0; i < indexes.size(); i++) {
            int count = 0;
            for(int j = indexes[i]; j < s.length(); j++) {
                if(is_vowel(s[j]))
                count++;
                else
                break;
            }
            string_sizes.push_back(count);
        }
    }
    else if(!is_vowel(s[0]) && is_vowel(s[s.length() - 1])) {
        // cout << "Inside 2nd if" << "\n";
        for(int i = 0; i < indexes.size() - 1; i++) {
            int count = 0;
            for(int j = indexes[i]; j < s.length(); j++) {
                if(is_vowel(s[j]))
                count++;
                else
                break;
            }

            for(int j = indexes[indexes.size() - 1]; j < s.length(); j++) {
                count++;
            }
            string_sizes.push_back(count);
        }
    }
    else if(is_vowel(s[0]) && !is_vowel(s[s.length() - 1])) {
        // cout << "Inside 3rd if" << "\n";
        for(int i = 1; i < indexes.size(); i++) {
            int count = 0;

            for(int j = indexes[0]; j < s.length(); j++) {
                if(is_vowel(s[j])) {
                    count++;
                }
                else {
                    break;
                }
            }
            for(int j = indexes[i]; j < s.length(); j++) {
                if(is_vowel(s[j]))
                count++;
                else
                break;
            }
            string_sizes.push_back(count);
        }
    }
    else {
        // cout << "Inside 4th if" << "\n";
        for(int i = 1; i < indexes.size() - 1; i++) {
            int count = 0;

            for(int j = indexes[0]; j < s.length(); j++) {
                if(is_vowel(s[j])) {
                    count++;
                }
                else {
                    break;
                }
            }
            for(int j = indexes[i]; j < s.length(); j++) {
                if(is_vowel(s[j]))
                count++;
                else
                break;
            }

            for(int j = indexes[indexes.size() - 1]; j < s.length(); j++) {
                count++;
            }
            string_sizes.push_back(count);
        }
    }
    // cout << "String sizes array: " << "\n";
    // for(int i = 0; i < string_sizes.size(); i++) {
    //     cout << string_sizes[i] << " ";
    // }
    // cout << "\n";

    int final_max = *max_element(string_sizes.begin(), string_sizes.end());
    
    cout << final_max << "\n";

    // if(is_vowel(s[0]))
    //     prev = 'v';

    // for(int i = 0; i < s.length(); i++) {
    //     if(is_vowel(s[i])){
    //         count++;
    //     }
    //     else {
    //         start = i;
    //         break;
    //     }
    // }
    // int no_of_sub = 0;
    // for(int i = start; i < s.length(); i++) {
    //     if(is_vowel(s[i])){
    //         prev = 'v';
    //         count++;
    //     }
    //     else {
            
    //     }
    // }
}


int main() {
    int t;
    
    cin >> t;

    while(t--) {
        string s;
        cin >> s;

        prob_chars(s);
    }
}