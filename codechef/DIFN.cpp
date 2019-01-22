#include <bits/stdc++.h>

using namespace std;

struct node {
    int data;
    bool visited;

    node() {
        data = 1;
        visited = false;
        // inQueue = false;
    }
};


bool areDistinct(vector< pair<string, int> > arr) {
    int n = arr.size();
    // Put all array elements in a map
    map<int, bool> s ;
    for(int i=0; i<n; i++){
       s.insert(pair<int, bool>(arr[i].second,true));
    }

    // If all elements are distinct, size of
    // map should be same array.
    return (s.size() == arr.size());
}

vector<int> problematicNodes(vector< pair<string, int> > arr) {
    int n = arr.size();
    vector<int> v;
    // Put all array elements in a map
    map<int, int> s;
    for(int i=0; i<n; i++){
//        s.insert(pair<int, int>(arr[i].second,true));
        s.find(arr[i].second) == s.end() ? (s[arr[i].second] = 1) : (s[arr[i].second]++);
    }

    for(map<int, int>::iterator it = s.begin(); it != s.end(); it++) {
        if(it->second > 1) {
            v.push_back(it->first);
        }
    }
    return v;
}



void diff_neighbours(node** arr, int N, int M) {
    vector<string> q;
    // arr[0][0].data = 1;
    arr[0][0].visited = true;
    // arr[0][0].inQueue = true;
    if(N == 1 && M == 1) {
        cout << 1 << "\n";
        cout << 1 << "\n";
        return;
    }
    else if(N == 1) {
        q.push_back("0 1");
        arr[0][1].visited = true;
        // arr[0][1].data = 1;
    }
    else if(M == 1) {
        q.push_back("1 0");
        arr[1][0].visited = true;
        // arr[1][0].data = 1;
    }
    else {
        q.push_back("0 1");
        q.push_back("1 0");
        arr[0][1].visited = true;
        arr[1][0].visited = true;
        // arr[0][1].data = 1;
        arr[1][0].data = 2;
    }

    while(!q.empty()) {
        vector< pair<string, int> > m;
        string ele = q.front();
        char ar[ele.length() + 1];
        strcpy(ar, ele.c_str());
        q.erase(q.begin());

        char token1 = *strtok(ar, " ");
        int row = token1 - '0';
        int row_copy = row;
        cout << "Row: " << row << "\n";
        token1 = *strtok(NULL, " ");
        int col = token1 - '0';
        int col_copy = col;
        cout << "Col: " << col << "\n";

        arr[row][col].visited = true;

        vector<string> nei;

        for(int i = 0; i < 4; i++) {
            if(i == 3) {
                row = row_copy;
                col = col_copy;
                row = row - 1;
            }
            else if(i == 2) {
                row = row_copy;
                col = col_copy;
                col = col - 1;
            }
            else if(i == 0) {
                row = row_copy;
                col = col_copy;
                col = col + 1;
            }
            else {
                row = row_copy;
                col = col_copy;
                row = row + 1;
            }
            cout << "Row1: " << row << "\n";
            cout << "Col1: " << col << "\n";
            if((row >= 0 && row < N) && (col >= 0 && col < M) && (row != row_copy || col != col_copy)) {
                string index = to_string(row) + " " + to_string(col);
                cout << "Neighbour of " << ele << ": " << index << "\n";
                m.push_back(make_pair(index, arr[row][col].data));
            }
        }


        vector<string> v;
        cout << "Hashmap: " << "\n";
        int same, same1 = -1, prev;
        for(int it = 0; it < m.size(); it++) {
            char ar1[ele.length() + 1];
            strcpy(ar1, m[it].first.c_str());
            token1 = *strtok(ar1, " ");
            row = token1 - '0';
            token1 = *strtok(NULL, " ");
            col = token1 - '0';

            if(!areDistinct(m)) {
                vector<int> conflictValue = problematicNodes(m);

                for(int p = 0; p < conflictValue.size(); p++) {
                    prev = 1;
                    if(m[it].second == conflictValue[p]) {
                        while (true) {
                            int flag = 0;
                            for (int it1 = 0; it1 < m.size(); it1++) {

                                int val = m[it1].second;
                                if (prev + 1 == val && m[it].first != m[it1].first) {
                                    flag = 1;
                                    break;
                                }
                            }
                            if (flag == 0) {
                                arr[row][col].data = prev + 1;
                                m[it].second = prev + 1;
                                break;
                            }
                            prev++;
                        }
                    }
                }
                
            }


            if(arr[row][col].visited == false) {
                arr[row][col].visited = true;
                string index = to_string(row) + " " + to_string(col);
                q.push_back(index);
            }

            cout << m[it].first << " = " << m[it].second << "\n";
        }

        cout << "Array: " << "\n";
        for(int j = 0; j < N; j++) {
            for(int k = 0; k < M; k++) {
                cout << arr[j][k].data << "\t";
            }
            cout << "\n";
        }

        cout << "Queue: " << "\n";
        for(int i = 0; i < q.size(); i++) {
            cout << q[i] << " - ";
        }
        cout << "\n";
        cout << "----------------------------------" << "\n";
        // q.erase(q.begin());
    }

    cout << "Final Array: " << "\n";
    for(int j = 0; j < N; j++) {
        for(int k = 0; k < M; k++) {
            cout << arr[j][k].data << "\t";
        }
        cout << "\n";
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

        node** arr = new node*[N];
        for(int j = 0; j < N; j++) {
            arr[j] = new node[M];
        }

        // for(int j = 0; j < N; j++) {
        //     for(int k = 0; k < M; k++) {
        //         arr[j][k] = 1;
        //     }
        // }

        diff_neighbours(arr, N, M);
    }



    return 0;
}