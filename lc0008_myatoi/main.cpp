#include <string>
#include <queue>
#include <iostream>
#include <vector>
#include "utils.h"

using namespace std;

class Solution {
public:
    bool is_digit(char c) {
        return (c >= '0' && c <= '9');
    }

    int myAtoi(string s) {
        long long result = 0;
        int sign = 1;

        int i = 0;
        while (s[i] == ' ') i++;

        if (s[i] == '+') sign = 1;
        else if (s[i] == '-') sign = -1;
        else if (!is_digit(s[i])) return 0;

        if (!is_digit(s[i])) i++;

        long long max_limit = (1LL << 31) - 1;
        long long min_limit = - (1LL << 31);
        while (is_digit(s[i])) {
            int dig = sign * (s[i] - '0');
            if (result * 10 <= min_limit - dig) {
                return min_limit;
            }
            if (result * 10 >= max_limit - dig) {
                return max_limit;
            }

            result *= 10;
            result += dig;
            i++;
        }

        return result;
    }
};

int main() {
    Solution sol;
    string tests[] = {"42", " -042", "1337c0d3", "0-1", "words and 987", "21474836460", "2147483646"};

    for (auto str : tests) {
        cout << sol.myAtoi(str) << endl;
    }

    return 0;
}
