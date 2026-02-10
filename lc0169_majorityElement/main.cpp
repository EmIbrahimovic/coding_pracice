#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt = 0, maj = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == maj) {
                cnt++;
            } else {
                cnt--;
                if (cnt < 0) { 
                    maj = nums[i];
                }
            }
        }

        return maj;
    }
};

int main() {
    Solution sol;
    /* input type + inputs needed */
    vector<int> tests[] = {
        {1, 1, 1, 2}
    };

    // Use utils if complex output
    for (auto test : tests) {
        cout << sol.majorityElement(test) << endl;
    }

    return 0;
}

