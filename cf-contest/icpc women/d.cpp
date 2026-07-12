#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>

using namespace std;

int main() {
    int n;
    double x;
    cin >> n >> x;

    vector<double> c(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }

    int first_drink_i = max_element(c.begin(), c.end()) - c.begin();

    double total_time = 0;
    for (int i = 0; i < n; i++) {
        if (i != first_drink_i && n > 1)
            total_time += log2(c[i]/ x + 1);
        else 
            total_time += log2(c[i] / x);
    }

    printf("%.10f\n", total_time);

    return 0;
}
