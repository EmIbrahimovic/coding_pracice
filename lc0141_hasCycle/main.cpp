#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* t = head;
        ListNode* h = head;

        int step = 0;
        while (step == 0 || h != t) {
            if (t != NULL && t->next != NULL) t = t->next->next;
            else return false;
            h = h->next;

            step++;
        }

        return true;
    }
};

int main() {
    Solution sol;
    /* input type + inputs needed */
    ListNode* tests[] = {

    };

    // Use utils if complex output
    for (auto test : tests) {
        cout << sol.hasCycle(test) << endl;
    }

    return 0;
}

