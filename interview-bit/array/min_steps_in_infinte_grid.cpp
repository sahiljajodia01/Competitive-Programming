int Solution::coverPoints(vector<int> &A, vector<int> &B) {
    int total = 0;
    for(int i = 1; i < A.size(); i++) {
        int max;
        if(abs(A[i] - A[i-1]) > abs(B[i] - B[i-1])) {
            total += abs(A[i] - A[i-1]);
        }
        else if(abs(B[i] - B[i-1]) > abs(A[i] - A[i-1])) {
            total += abs(B[i] - B[i-1]);
        }
        else {
            total += abs(B[i] - B[i-1]);
        }
    }
    
    return total;
}