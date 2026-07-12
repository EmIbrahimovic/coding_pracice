#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> p(n);
    int maxP = INT_MIN;
    for (int i = 0; i < n; i++) {
        cin >> p[i];

        if (i >= k) {
            maxP = max(maxP, p[i] - p[i - k]);
        }
    }

    cout << maxP << endl;

    return 0;
}
