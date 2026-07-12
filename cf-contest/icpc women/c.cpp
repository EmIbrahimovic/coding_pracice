#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<unsigned long long, unsigned long long> > times(n);
    for (int i = 0; i < n; i++) {
        unsigned long long t, d, c;
        cin >> t >> d >> c;

        times[i] = make_pair(t + d, c);
    }

    sort(times.begin(), times.end());
    
    unsigned long long currtime = 0;
    for (int i = 0; i < n; i++) {
        if (times[i].first > currtime) {
            currtime = times[i].first;
        }
        currtime += times[i].second;
    }

    cout << currtime << endl;

    return 0;
}
