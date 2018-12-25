long long combine(vector<int> &arr, int beg, int mid, int end) {
    int i = beg;
    int j = mid+1;
    int temp[end-beg+1];
    int index = beg;
    long long inversions = 0;
    while(i<=mid && j<=end) {
        if(arr[i] < arr[j]) {
            temp[index] = arr[i];
            i++;
            index++;
        }
        else {
            temp[index] = arr[j];
            j++;
            index++;
            inversions += mid - i + 1;
        }
    }

    if(i > mid) {
        for(int k = j; k <= end; k++) {
            temp[index] = arr[j];
            j++;
            index++;
        }
    }
    else {
        for(int k = i; k <= mid; k++) {
            temp[index] = arr[i];
            i++;
            index++;
        }
    }

    for(int k = beg; k < index; k++) {
        arr[k] = temp[k];
        // cout << "Sorted Elements: " << v[k] << " ";
    }
    return inversions;
}

long long mergesort(vector<int> &arr, int beg, int end) {
    long long inversions = 0;
    long long zero = 0;
    if(beg < end) {
        int mid = (beg+end)/2;
        inversions += mergesort(arr, beg, mid);
        inversions += mergesort(arr, mid+1, end);
        inversions += combine(arr, beg, mid, end);
        return inversions;
    }
    else {
        return zero;
    }
}

// Complete the countInversions function below.
long long countInversions(vector<int> arr) {
    long long count;
    count = mergesort(arr, 0, arr.size() - 1);
    cout << "Sorted Array: " << "\n";
    for(int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
    return count;
}