#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int f, y, b, m, s;
    cin >> f >> y >> b >> m >> s;
    int fa, ya, ba, ma, sa;
    cin >> fa >> ya >> ba >> ma >> sa;

    vector<int> nums = {fa / f, ya / y, ba / b, ma / m, sa / s};
    int numbuns = *min_element(nums.begin(), nums.end());
    cout << numbuns << endl;

    return 0;
}
