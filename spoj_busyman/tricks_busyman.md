---
strongly-connected:
- "[[spoj]]"
- "[[job scheduling]]"
- "[[greedy]]"
tags:
- problem
favorite: False
---

# SPOJ 278. busyman

classic activity selection problem, did it in 1220.

implementation via priority queue

## approach lessons



## cpp optimizations

pq initialization with custom comparator (lambda instread of struct!):
```cpp
auto finish_comp = [](const pair<int, int>& z1, const pair<int, int>& z2) {
    return (z1.second == z2.second) ? (z1.first > z2.first) : (z1.second > z2.second);
};
priority_queue<pair<int, int>, vector< pair<int, int>>, decltype(finish_comp)> pq {finish_comp, activities};
```
