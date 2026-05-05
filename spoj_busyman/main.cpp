#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include "utils.h"

using namespace std;

class Solution {
public:

    int busyman(int n, vector<pair<int, int> > activities) {
        auto finish_comp = [](const pair<int, int>& z1, const pair<int, int>& z2) {
            return (z1.second == z2.second) ? (z1.first > z2.first) : (z1.second > z2.second);
        };
        priority_queue<pair<int, int>, vector< pair<int, int>>, decltype(finish_comp)> pq {finish_comp, activities};

        int max_activities = 0;
        int last_finish = -1;
        while (!pq.empty()) {
            pair<int, int> act = pq.top();
            pq.pop();

            if (act.first < last_finish) continue;
            else {
                max_activities++;
                last_finish = act.second;
            }
        }

        return max_activities;
    }
};

int main() {
    Solution sol;
    /* input type + inputs needed */
    pair<int, vector<pair<int, int> >> tests[] = {
        {3, {{3, 9}, {2, 8}, {6, 9}}},
        {4, {{1, 7}, {5, 8}, {7, 8}, {1, 8}}},
        {6, {{7, 9}, {0, 10}, {4, 5}, {8, 9}, {4, 10}, {5, 7}}}
    };

    // Use utils if complex output
    for (auto test : tests) {
        cout << sol.busyman(test.first, test.second) << endl;
    }

    return 0;
}
