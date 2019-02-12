// Still do not get all the test cases correct


#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
#define pdd pair<double, double>

pdd lineLineIntersection(pdd A, pdd B, pdd C, pdd D) 
{ 
	// Line AB represented as a1x + b1y = c1 
	double a1 = B.second - A.second; 
	double b1 = A.first - B.first; 
	double c1 = a1*(A.first) + b1*(A.second); 

	// Line CD represented as a2x + b2y = c2 
	double a2 = D.second - C.second;
	double b2 = C.first - D.first; 
	double c2 = a2*(C.first)+ b2*(C.second); 

	double determinant = a1*b2 - a2*b1; 

	if (determinant == 0) 
	{ 
		// The lines are parallel. This is simplified 
		// by returning a pair of FLT_MAX 
		return make_pair(FLT_MAX, FLT_MAX); 
	} 
	else
	{ 
		double x = (b2*c1 - b1*c2)/determinant; 
		double y = (a1*c2 - a2*c1)/determinant; 
		return make_pair(x, y); 
	} 
}


int main() {
	ll t;

	cin >> t;

	while(t--) {
		// ll q = 12345;

		ll check, xl, yl, xh, yh, check2, ans, x, y, check3, check4;

		cout << "Q " << "0 " << "0" << endl;
		cout << flush;

		cin >> check;

		cout << "Q " << "0 " << "1000000000" << endl;
		cout << flush;

		cin >> check2;

	   	// cout << "Q " << "0 " << check2 << endl;
	   	// cout << flush;

	   	// cin >> check3;
		ll temp = 2*1000000000 - check2;

		pdd A = make_pair(0, check); 
		pdd B = make_pair(check, 0); 
		pdd C = make_pair(check - temp, 0); 
		pdd D = make_pair(check, temp);

		pdd intersection = lineLineIntersection(A, B, C, D);


	    // ll second = (1000000000 - check2/2);

	    cout << "Q " << "0 " << (int)intersection.second << endl;
	    cout << flush;

	    cin >> check4;

	    // if(check3 < check4) {
	    // 	check4 = check3;
	    // }

	    xl = check4;
		yl = check - check4;
		// }


		// xl = (0 + check2);
		// yl = (check - check2);

		cout << "Q " << "1000000000 " << "1000000000" << endl;
		cout << flush;

		cin >> check;

		cout << "Q " << "1000000000 " << yl << endl;
		cout << flush;


		cin >> check2;

		xh = (1000000000 - check2);
		yh = (1000000000 - check + check2);

		cout << "A " << xl << " " << yl << " " << xh << " " << yh << endl;
		cout << flush;

		cin >> ans;

		if(ans > 0)
			continue;
		else
			break;
	}

	return 0;
}