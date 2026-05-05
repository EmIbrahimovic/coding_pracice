
## priority queue

syntactic stuff
https://en.cppreference.com/cpp/container/priority_queue
#### [[custom comparator]] - class
#### custom comparator - lambda
```cpp
auto finish_comp = [](const pair<int, int>& z1, const pair<int, int>& z2) {
	return (z1.second == z2.second) ? (z1.first > z2.first) : (z1.second > z2.second);
};

priority_queue<pair<int, int>, vector< pair<int, int>>, decltype(finish_comp)> pq {finish_comp, activities};
```
used in [[tricks_busyman]]