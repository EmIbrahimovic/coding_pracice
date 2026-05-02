---
strongly-connected:
  - "[[python]]"
---

# SortedList

[[SortedList]]

# SortedDict

[[SortedDict]]

# OrderedDict

#### Time Complexity

| Operation             | Complexity |
| --------------------- | ---------- |
| `get` / `__getitem__` | O(1)       |
| `set` / `__setitem__` | O(1)       |
| `del` / `__delitem__` | O(1)       |
| `move_to_end`         | O(1)       |
| `popitem`             | O(1)       |
| Iteration             | O(n)       |
| Equality check        | O(n)       |
Internally it's a hash map + a doubly linked list (for ordering), so all the core operations stay O(1) while maintaining position awareness. The tradeoff is slightly higher memory overhead than a plain dict.

# heapq
