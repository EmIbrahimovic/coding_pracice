#include <string>
#include <map>
#include <iostream>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) return 0;

        // unordered_map<char, int> indices;
        vector<int> indices(260, -1);
        int start = 0, max_len = 1;
        indices[s[0] - 'a'] = 0;
        for (int i = 1; i < (int)s.size(); i++) {
            int last_occ = indices[s[0] - 'a'];
            // if (indices.count(s[i]) > 0)
            //     last_occ = indices[s[i]];

            start = max(last_occ + 1, start);
            max_len = max(i - start + 1, max_len);
            
            indices[s[i] - 'a'] = i;
        }
        return max_len;
    }
};

int main() {

    string test_str = "pwwkew";
    Solution sol;

    cout << sol.lengthOfLongestSubstring(test_str) << endl;

    return 0;
}
