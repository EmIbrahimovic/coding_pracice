#include <iostream>
#include <string>
#include <vector>
#include "utils.h"

using namespace std;


/**
Definition for singly-linked list.
*/
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if (head == NULL) {
            return NULL;
        }

        ListNode* ptr = head;
        ListNode* middle = head;
        int indx = 0;
        while (ptr != NULL) {
            ptr = ptr->next;

            if (indx % 2 == 1) middle = middle->next;
            indx++;
        }

        return middle;
    }
};

int main() {
    Solution sol;
    /* input type + inputs needed */
    ListNode* headNode1 = new ListNode(0);
    ListNode* headNode2 = new ListNode(0, new ListNode(1));
    ListNode* headNode3 = new ListNode(0, new ListNode(1, new ListNode(2)));

    ListNode* tests[] = {
        nullptr,
        headNode1,
        headNode2,
        headNode3
    };

    // Use utils if complex output
    for (auto test : tests) {
        ListNode* solsol = sol.middleNode(test);
        if (solsol != 0)
            cout << solsol->val << endl;
        else
            cout << "nullptr" << endl;
    }

    return 0;
}

