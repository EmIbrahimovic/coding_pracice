#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include "utils.h"

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        vector<int> rMax(n, -1), lMax(n, -1);
        rMax[0] = height[n - 1]; // let's get ready for some MESS
        lMax[0] = height[0];
        int maxVol = 0;
        
        // Look for poles on the RIGHT
        for (int i = n - 2; i >= 0; i--) {
            rMax[n - 1 - i] = max(rMax[n - 2 - i], height[i]);

            // cout << height[i] << endl;
            int pos = lower_bound(rMax.begin(), rMax.begin() + (n - i), height[i]) - rMax.begin();
            int actual = n - 1 - pos;
            // print_vector(rMax);
            // cout << pos << " " << actual << endl;

            maxVol = max(maxVol, height[i] * (actual - i));
        }
        // Look for poles on the RIGHT
        for (int i = 1; i < n; i++) {
            lMax[i] = max(lMax[i - 1], height[i]);

            // cout << height[i] << endl;
            int pos = lower_bound(lMax.begin(), lMax.begin() + i + 1, height[i]) - lMax.begin();
            // print_vector(lMax);
            // cout << pos << endl;

            maxVol = max(maxVol, height[i] * (i - pos));
        }

        return maxVol;
    }
};

int main() {
    Solution sol;
    vector<int> tests[] = {
        {1,8,6,2,5,4,8,3,7},
        {2,1},
        {1},
        {2, 1, 3},
        {5, 5, 5, 5, 5},
        {1, 7, 1},
        {8,7,2,1}
    };

    for (auto test : tests) {
        cout << sol.maxArea(test) << endl;
    }

    return 0;
}

