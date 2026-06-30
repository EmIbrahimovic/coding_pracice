#include <bits/stdc++.h>

using namespace std;

int log2(int n) {
    int i = 0;
    while (n > 1) {
        n /= 2;
        i++;
    }
    return i;
}

int pow2(int n) {
    int i = 1;
    while (n) {
        i *= 2;
        n--;
    }
    return i;
}

int getAns(int n, int k) {
    if (k == 0) {
        return 0;
    }
    if (n <= k) {
        return n;
    } 

    int avg = n / k;
    int num = log2(avg + 1);

    return num + getAns(n - (pow2(num) - 1), k - 1);
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        cout << getAns(n, k) << endl;
    }


    return 0;
}
