#include <vector>
#include <algorithm>
#include <set>
#include <cstdio>
// #include <utils.h>

using namespace std;

int main() {

    int n, k;
    scanf("%d %d", &n, &k);

    vector<pair<int, int> > movies(n);
    for (int i = 0; i < n; i++) scanf("%d %d", &movies[i].first, &movies[i].second);

    auto mycomp = [](const pair<int, int>& p1, const pair<int, int>& p2){
        return p1.second < p2.second;
    };
    sort(movies.begin(), movies.end(), mycomp);

    // vector<int> finish_times;

    // this multiset contains 0 0 0 f1 f2 f3 .. fk-x
    // where the the f-s are the finish times of intervals
    // we hold the invariant: at all times t < f1, there are exactly k - x chosen intervals overlapping;
    // at all times t >= f1, there are < k - x chosen intervals overlapping
    // this means that at every t < f1, there are some k chosen intervals which overlap

    // if an incoming s, f has s < f1, it's going to overlap some k intervals and that's not good. we don't choose it.
    // if an incoming s, f has fi < s < fi+1, then at all of its points it overlaps with < k intervals.
    // the f of every new interval added to the winning set is always added. 
    // in return, one of the other fs is deleted.
    // this corresponds to the fact that if the latest interval overlapps with k intervals at some time point
    // then 
    int num_selections = 0;
    multiset<int> finish_times;
    for (int i = 0; i < k; i++) finish_times.insert(0);

    for (int i = 0; i < n; i++) {
        
        auto last_overlapping = upper_bound(finish_times.begin(), finish_times.end(), movies[i].first);
        
        if (last_overlapping == finish_times.begin()) {
            continue;
        }

        last_overlapping--;

        finish_times.erase(last_overlapping);
        finish_times.insert(movies[i].second);
        num_selections++;
    }

    printf("%d\n", num_selections);

    return 0;
}
