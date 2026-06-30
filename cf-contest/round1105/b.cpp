#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

const ull MOD = 998244353;

ull pow2(ull n) {
    if (n == 0) {
        return 1;
    }
    if (n % 2 == 0) {
        ull x = pow2(n / 2);
        return (x * x) % MOD;
    }
    return (2 * pow2(n - 1)) % MOD;
}

ull getAns(ull n, ull m, ull r, ull c) {
    ull pp = r * c - 1 + (c - 1) * (n - r) + (r - 1) * (m - c);
    // cout << pp << endl;
    return pow2(pp);
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        ull n, m, r, c;
        cin >> n >> m >> r >> c;

        cout << getAns(n, m, r, c) << endl;
    }

    return 0;
}
