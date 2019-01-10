#include <bits/stdc++.h>
#define gc getchar_unlocked

using namespace std;

void distinct_pairs(vector<int> a, vector<int> b) {
	map<int, int> sum;
	int a_size = a.size();
	int b_size = b.size();
	vector< pair <int,int> > vect;

	// for(int i = 0; i < a.size(); i++) {
	// 	if(m1.find(a[i]) == m1.end()) {
	// 		m1[a[i]] = 1;
	// 	}
	// }

	// for(int i = 0; i < b.size(); i++) {
	// 	if(m2.find(b[i]) == m2.end()) {
	// 		m2[b[i]] = 1;
	// 	}
	// }
	int count = 0;
	int flag1 = 0, flag2 = 0;
	if(a_size == b_size) {
		int i;
		for(i = 1; i < a_size; i++) {
			if(a[i] != a[i-1] + 1) {
				break;
			}
		}
		if(i == a_size) {
			flag1 = 1;
		}

		for(i = 1; i < b_size; i++) {
			if(b[i] != b[i-1] + 1) {
				break;
			}
		}
		if(i == b_size) {
			flag2 = 1;
		}

	}
	// map<int, int>::iterator it1 = m1.begin();
	// map<int, int>::iterator it2 = m2.begin();
	if(flag1 == 1 && flag2 == 1) {
		for(int i = 0; i < a_size; i++) {
			printf("0 %d\n", i);
		}
		for(int i = 1; i < a_size; i++) {
			printf("%d %d\n", i, a_size - 1);
		}
	}
	else {
		for(int i = 0; i < a_size; i++) {
			if(count < (a_size + b_size - 1)) {
				for(int j = 0; j < b_size; j++) {
					if(count < (a_size + b_size - 1)) {
						if(sum.find(a[i] + b[j]) == sum.end()) {
							sum[a[i] + b[j]] = 1;
							// vect.push_back( make_pair(i, j) );
							printf("%d %d\n", i, j);
							count++;
						}
						else {
							sum[a[i] + b[j]]++;
						}
					}
					else {
						break;
					}
				}
			}
			else {
				break;
			}
		}
	}

	// map<int, int>::iterator it1 = sum.begin();
	// cout << "Map: " << "\n";
	// while(it1 != sum.end()) {
	// 	cout << it1->first << "-" << it1->second << "\n";
	// 	it1++;
	// }


	// cout << "VEct size: " << vect.size() << "\n";

	// for(int i = 0; i < a_size + b_size - 1; i++) {
	// 	printf("%d %d\n", vect[i].first, vect[i].second);
	// }

	// int count1 = 0, count2 = 0;
	// while(true) {
	// 	for(int i = count2; i < a_size; i++) {
	// 		// if(count < (a.size() + b.size() - 1)) {
	// 			if(sum.find(a[i] + b[count1]) == sum.end()) {
	// 				sum[a[i] + b[count1]] = 1;
	// 				printf("%d %d\n", i, count1);
	// 				count++;
	// 			}
			// }
			// else {
			// 	break;
			// }
		// }

		// map<int, int>::iterator it1 = c.begin();
		// while(it1 != c.end()) {
		// 	cout << "C: " << it1->first << "\n";
		// 	it1++;
		// }

		// for(int i = count1+1; i < b_size; i++) {
		// 	// if(count < (a.size() + b.size() - 1)) {
		// 		if(sum.find(a[count2] + b[i]) == sum.end()) {
		// 			sum[a[count2] + b[i]] = 1;
		// 			printf("%d %d\n", count2, i);
		// 			count++;
		// 		}
			// }
			// else {
			// 	break;
			// }
		// }
		// count1++;
		// count2++;
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
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	int N, M;
	// scanf("%d %d", &N, &M);
	scanint(N);
	scanint(M);
	vector<int> a, b;

	for(int i = 0; i < N; i++) {
		int temp;
		// scanf("%d", &temp);
		scanint(temp);
		a.push_back(temp);
	}

	for(int i = 0; i < M; i++) {
		int temp;
		// scanf("%d", &temp);
		scanint(temp);
		b.push_back(temp);
	}

	distinct_pairs(a, b);

	return 0;
}