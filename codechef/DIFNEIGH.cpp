#include <bits/stdc++.h>

using namespace std;


void diff_neighbours(int** arr, int N, int M) {
    queue<string> q;

    q.push("0 1");
    q.push("1 0");

    while(!q.empty()) {
        map<int, int> m;
        string ele = q.front();
        char ar[ele.length() + 1];
        strcpy(ar, ele.c_str());
        q.pop();

        char token1 = *strtok(ar, " ");
        int row = token1 - '0';
        token1 = *strtok(NULL, " ");
        int col = token1 - '0';
        
        for(int i = 0; i < 4; i++) {
            if(i == 0) {
                row = row - 1;
            }
            else if(i == 1) {
                col = col - 1;
            }
            else if(i == 2) {
                col = col + 1;
            }
            else {
                row = row + 1;
            }

            if((row >= 0 && row < N) && (col >= 0 && col < M)) {
                if(m.find(arr[row][col]) == m.end()) {
                    m[arr[row][col]] = 1;
                }
                else {
                    m[arr[row][col]]++;
                }
            }
        }

        
        
    }


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

	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;

    scanint(t);

    for(int i = 0; i < t; i++) {

		int N, M;

		scanint(N);
		scanint(M);

		int** arr = new int*[N];
		for(int j = 0; j < N; j++) {
			arr[j] = new int[M];
		}

        for(int j = 0; j < N; j++) {
            for(int k = 0; k < M; k++) {
                arr[i][j] = 1;
            }
        }

		diff_neighbours(arr, N, M);
	}



	return 0;
}