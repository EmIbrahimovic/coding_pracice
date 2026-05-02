import typing
from collections import heapq
from collections import OrderedDict

class LRUCacheOld:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.cnt = 0
        self.rused = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cnt += 1
            self.cache[key] = (self.cache[key][0], self.cnt)
            heapq.heappush(self.rused, (self.cnt, key))
        
        return self.cache.get(key, (-1, -1))[0]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            to_evict = -1
            while to_evict == -1:
                to_evict = heapq.heappop(self.rused)
                if to_evict[0] < self.cache[to_evict[1]][1]:
                    to_evict = -1

            del self.cache[to_evict[1]]
        
        self.cnt += 1
        self.cache[key] = (value, self.cnt)
        heapq.heappush(self.rused, (self.cnt, key))


# Your LRUCache object will be instantiated and called as such:

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        while key not in self.cache and len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        
        self.cache[key] = value
        self.cache.move_to_end(key)


if __name__ == "__main__":
    sol = LRUCache(20)

    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)

    tests = [
        # Test Cases
    ]

    for t, test in enumerate(tests):
        print(f"======= Test {t} ========")
        answer = sol.lruCache(*test)
        print(answer)

