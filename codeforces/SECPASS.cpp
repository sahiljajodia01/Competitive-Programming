#include <bits/stdc++.h>

using namespace std;

void findAllOccurances(std::vector<size_t> & vec, std::string data, std::string toSearch)
{
	// Get the first occurrence
	size_t pos = data.find(toSearch);
 
	// Repeat till end is reached
	while( pos != std::string::npos)
	{
		// Add position to the vector
		vec.push_back(pos);
 
		// Get the next occurrence from the current position
		pos =data.find(toSearch, pos + toSearch.size());
	}
}


int main() {
    int t;

    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        string s;
        cin >> s;

        map<string, int> m;

        for(int i = 0; i < s.length(); i++) {
            
        } 
    }
}