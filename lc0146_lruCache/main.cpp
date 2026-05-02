#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include "utils.h"

using namespace std;


class LRUCache {
private: 
    int capacity;
    priority_queue<pair<int, int>, std::vector<pair<int, int> >, std::greater<pair<int, int> >> rused;
    int cnt = 0;
    map<int, pair<int, int> > cache;

public:

    LRUCache(int capacity_) {
        capacity = capacity_;
    }
    
    int get(int key) {
        if (cache.count(key)) {
            cnt++;
            cache[key] = make_pair(cache[key].first, cnt);
            rused.push(make_pair(cnt, key));

            cout << "Get returns:" << cache[key].first << endl;
            cout << "Assigning: " << cnt << " to cache together with value" << endl;
            return cache[key].first;
        }

        return -1;
    }
    
    void put(int key, int value) {
        if (cache.count(key) == 0 && cache.size() == capacity) {
            pair<int, int> to_evict = make_pair(-1, -1);

            // find the first non-stale value on the heap
            while (to_evict.first == -1) {
                to_evict = rused.top();
                rused.pop();
                if (to_evict.first < cache[to_evict.second].second) {
                    to_evict = make_pair(-1, -1);
                }
            }
            
            cout << "Put evicting " << to_evict.first << " " << to_evict.second << endl;
            cache.erase(to_evict.second);
        }
        cnt++;
        cache[key] = make_pair(value, cnt);
        rused.push(make_pair(cnt, key));
        cout << "Put assigns:" << value << " to " << key << endl;
        cout << "Assigning: " << cnt << " to cache together with value" << endl;
    }
};

int main() {
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

    int capacity = 2;
    LRUCache* obj = new LRUCache(capacity);

    obj->put(1, 1);
    obj->put(2, 2);
    obj->get(1);
    obj->put(3, 3);
    obj->get(2);
    obj->put(4, 4);
    obj->get(1);
    obj->get(3);
    obj->get(4);

    // int param_1 = obj->get(key);
    // obj->put(key,value);

    return 0;
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */