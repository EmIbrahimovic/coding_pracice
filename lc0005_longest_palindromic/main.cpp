#include <string>
#include <map>
#include <iostream>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() == 0) return "";

        int n = s.size();
        int max_len = 1, index = 0;
        vector<vector<bool> > isPalindome(n, vector<bool>(n, 0));
        for (int l = 1; l <= n; l++) {
            for (int i = 0; i < n - l + 1; i++) {
                if (l == 1) isPalindome[i][i] = 1;
                else if (l == 2) isPalindome[i][i + l - 1] = (s[i] == s[i + l - 1]);
                else isPalindome[i][i + l - 1] = (s[i] == s[i + l - 1]) & isPalindome[i + 1][i + l - 2];
                
                if (isPalindome[i][i + l - 1]) {
                    max_len = l;
                    index = i;
                }
            }
        }

        // cout << s.substr(index, max_len) << endl;
        return s.substr(index, max_len);
    }
};

int main() {

    string tests[] = {"babad", "aaaaa", "cbbd", "baaababcbaaab"};
    Solution sol;

    for (auto test_str : tests)
        cout << sol.longestPalindrome(test_str) << endl;

    return 0;
}
