#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(/* input needed */) {
        ListNode* result;

        return result;
    }
};

int main() {
    Solution sol;
    /* input type + inputs needed */
    int tests[] = {

    };

    // Use utils if complex output
    for (auto test : tests) {
        cout << sol.mergeTwoLists(test) << endl;
    }

    return 0;
}

