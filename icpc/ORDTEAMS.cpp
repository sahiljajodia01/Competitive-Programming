#include<bits/stdc++.h>

using namespace std;

struct values {

	values(int v1_, int v2_, int v3_)
        : v1(v1_), v2(v2_), v3(v3_)
    {}

	int v1;
	int v2;
	int v3;
};

bool compareAge(const values &lhs, const values &rhs)
{
    if(lhs.v1 <= rhs.v1 && lhs.v2 <= rhs.v2 && lhs.v3 <= rhs.v3) {
    	return true;
    }
    else {
    	return false;
    }
}


int main() {
	list<values> persons;

	persons.push_back(values(2, 4, 6));
	persons.push_back(values(2, 3, 7));
	persons.push_back(values(1, 2, 3));


	persons.sort(&compareAge);

	for(list<values>::iterator it = persons.begin(); it != persons.end(); it++) {
		cout << it->v1 << it->v2 << it->v3 << "\n";
	}
}


int compare(int a[], int b[]) {
	if(a[0] >= b[0] && a[1] >= b[1] && a[2] >= b[2]) {
		for(int i = 0; i < 3; i++) {
			if(a[i] > b[i]) {
				return 1;
			}
		}
		return 0;
	}
	else if(a[0] <= b[0] && a[1] <= b[1] && a[2] <= b[2]) {
		for(int i = 0; i < 3; i++) {
			if(a[i] < b[i]) {
				return 2;
			}
		}
		return 0;
	}
	else {
		return 0;
	}
}


