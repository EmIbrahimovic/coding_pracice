#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(n + 1, 0);
        dp[0] = 1;

        for (int i = 0; i < n; i++) {
            for (auto word : wordDict) {
                int l = word.size();
                if ((i + 1 - l >= 0) && s.substr(i + 1 - l, l) == word) {
                    dp[i + 1] = dp[i + 1 - l];
                    if (dp[i + 1]) break;
                }
            }
        }

        return dp[n];
    }
};

int main() {
    Solution sol;
    /* input type + inputs needed */
    pair<string, vector<string> > tests[] = {
        {"leetcode", {"leet", "code"}},
        {"applepenapple", {"apple", "pen"}},
        {"catsandogs", {"cats", "sand", "and", "dogs"}}
    };

    // Use utils if complex output
    for (auto test : tests) {
        cout << sol.wordBreak(test.first, test.second) << endl;
    }

    return 0;
}

