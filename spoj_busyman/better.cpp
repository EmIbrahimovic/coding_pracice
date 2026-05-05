#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {

    int t;
    cin >> t;

    while (t--) {

        int n; 
        cin >> n;
        vector<pair<int, int> > activities(n);
        for (int i = 0; i < n; i++) {
            cin >> activities[i].first >> activities[i].second;
        }

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

        cout << max_activities << endl;

    }

    return 0;
}
