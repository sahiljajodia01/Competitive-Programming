#include <bits/stdc++.h>

using namespace std;


struct Node {
	int pairs;
	int open;
	int closed;

	Node() {
		pairs = open = closed = 0;
	}

};

int getMid(int start, int end) {
	return start + (end - start)/2;
}

Node merge(Node left, Node right) {
	Node parent;
	int minMatch = min(left.open, right.closed);
	parent.pairs = left.pairs + right.pairs + minMatch;
	parent.open = left.open + right.open - minMatch;
	parent.closed = left.closed + right.closed - minMatch;
	return parent;
}

void constructSTUtil(string str, int ss, int se, Node* st, int index) {
	if(ss == se) {
		st[index].pairs = 0;

		st[index].open = (str[ss] == '(' ? 1 : 0);
		st[index].closed = (str[ss] == ')' ? 1 : 0);

		return;
	}

	int mid = getMid(ss, se);
	constructSTUtil(str, ss, mid, st, 2*index);
	constructSTUtil(str, mid+1, se, st, 2*index+1);

	st[index] = merge(st[2*index], st[2*index + 1]);
}

Node* constructST(string str, int n) {
	int max_size = 2*n;

	Node* st = new Node[max_size];

	constructSTUtil(str, 0, n-1, st, 1);

	return st;
}


Node queryUtil(Node* st, int ss, int se, int qs, int qe, int index) {
	if(qs > se || qe < ss) {
		Node null;
		return null;
	}

	if(ss >= qs && se <= qe) {
		return st[index];
	}

	int mid = getMid(ss, se);
	Node left = queryUtil(st, ss, mid, qs, qe, 2*index);
	Node right = queryUtil(st, mid+1, se, qs, qe, 2*index + 1);

	Node ans = merge(left, right);
	return ans;
}


int query(Node* st, int qs, int qe, int n) {
	Node ans = queryUtil(st, 0, n-1, qs, qe, 1);

	return 2*ans.pairs;
}


// void build_tree(int* a, int* tree, int start, int end, int node) {
// 	if(l == r) {
// 		tree[node] = 0;
// 	}
// 	else {
// 		int mid = start - (start - end)/2;
// 		build_tree(a, tree, start, mid, 2*node);
// 		build_tree(a, tree, mid+1, end, 2*node+1);

// 		for(int )
// 	}
// }

int main() {
	int t;
	cin >> t;

	for(int i = 0; i < t; i++) {
		string str;
		cin >> str;
		// int* tree = new int[2*s.length()];

		Node* st = constructST(str, str.length());

		int start, end;
		cin >> start >> end;

		int ans = query(st, start, end, str.length());
		cout << ans << "\n";
	}

	return 0;
}