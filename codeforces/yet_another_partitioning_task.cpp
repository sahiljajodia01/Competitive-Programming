// 1114B

#include <bits/stdc++.h>

using namespace std;

void partitioning_task(vector<int> v, int m, int k) {
    int sum = 0;
    
    while(v.size() > 0) {
        int max = v.size() - k*m;
        int max_val = 0;
        int current = 0;

        for(int i = 0; i < m; i++) {
            current += v[i];
        }

        max_val = current;

        for(int i = m; i < max; i++) {
            vector<int> v_copy = v;
            sort(v_copy.begin(), v_copy.begin() + i);
            reverse(v_copy.begin(), v_copy.begin() + i);

            for(int j = i; j < i + m; j++) {
                current += v[j];
            }

            if(max_val < current) {
                max_val = current;
            }
        }

        sum += max_val;
    }

    cout << "Total sum: " << sum << "\n";

}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> v(n);

    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }

    partitioning_task(v, m, k);

    return 0;
}