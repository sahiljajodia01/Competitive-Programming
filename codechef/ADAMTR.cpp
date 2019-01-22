#include <bits/stdc++.h>

using namespace std;

vector< vector<int> > combinationUtil(int *arr, int data[], int start, int end, 
                     int index, int r, vector< vector<int> > v) 
{
    // Current combination is ready to be printed, print it 
    if (index == r)
    { 
    	// vector<int> v;
    	vector<int> w;
        for (int j=0; j<r; j++) {
        	w.push_back(data[j]);
        }
        v.push_back(w);
        // printf("\n"); 
        return v;
    } 
  
    // replace index with all possible elements. The condition 
    // "end-i+1 >= r-index" makes sure that including one element 
    // at index will make a combination with remaining elements 
    // at remaining positions 
    for (int i=start; i<=end && end-i+1 >= r-index; i++) 
    { 
        data[index] = arr[i]; 
        v = combinationUtil(arr, data, i+1, end, index+1, r, v); 
    } 

    return v;
} 



vector< vector<int> > printCombination(int *arr, int n, int r) 
{ 
    // A temporary array to store all combination one by one 
    int data[r];
    vector< vector<int> > v;
  
    // Print all combination using temprary array 'data[]' 
    v = combinationUtil(arr, data, 0, n-1, 0, r, v);
    return v;
} 
  
/* arr[]  ---> Input Array 
   data[] ---> Temporary array to store current combination 
   start & end ---> Staring and Ending indexes in arr[] 
   index  ---> Current index in data[] 
   r ---> Size of a combination to be printed */



void adamtr(vector< vector<int> > a, vector< vector<int> > b, int n) {
	// int count = (int)pow(2, n) - 1;
	int* arr = new int[n];
	vector< vector<int> > v;

	for(int i = 0; i < n; i++) {
		cout << "Hello" << "\n";
		v = printCombination(arr, n, i+1);
		for(int j = 0; j < v.size(); j++) {
			cout << "Hello 2" << "\n";
			vector<int> z = v[j];
			for(int k = 0; k < z.size(); k++) {
				cout << "Hello 3" << "\n";
				cout << z[k] << " ";
			}
			cout << "\n";
		}
	}
	// while(count != 0) {


	// 	count--;
	// }
}

inline void scanint(int &x) {
    register int c = getchar_unlocked();
    x = 0;
    int neg = 0;

    for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());

    if(c=='-') {
        neg = 1;
        c = getchar_unlocked();
    }

    for(; c>47 && c<58 ; c = getchar_unlocked()) {
        x = (x<<1) + (x<<3) + c - 48;
    }

    if(neg)
        x = -x;
}

int main() {
	int t;

	scanint(t);

	while(t--) {
		int n;

		vector< vector<int> > a;
		vector< vector<int> > b;

		scanint(n);

		for(int i = 0; i < n; i++) {
			vector<int> v;
			for(int j = 0; j < n; j++) {
				int temp;
				scanint(temp);
				v.push_back(temp);
			}
			a.push_back(v);
		}

		for(int i = 0; i < n; i++) {
			vector<int> v;
			for(int j = 0; j < n; j++) {
				int temp;
				scanint(temp);
				v.push_back(temp);
			}
			b.push_back(v);
		}


		adamtr(a, b, n);

	}


	return 0;
}