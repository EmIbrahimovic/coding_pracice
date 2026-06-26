---
strongly-connected:
  - "[[python]]"
---
![[python stdlib]]
# Counter

https://realpython.com/python-counter/
```python
from collections import Counter

s = "aabcd"
cnts = Counter(s)
# Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1})
```

```python
from collections import Counter

c = Counter("mississippi")
print(c)                 # counts each character
print(c.most_common(2))  # top 2
c.update("abc")
c.subtract("is")
print(c.total())
```

- `elements()`: yields each element repeated by its count, ignoring zero and negative counts.[](https://docs.python.org/3/library/collections.html)
- `subtract(iterable_or_mapping)`: subtracts counts; results can go to zero or negative.[](https://docs.python.org/3/library/collections.html)

# deque
https://docs.python.org/3/library/collections.html

```python
from collections import deque
```

```python
d[-1], d[0] # to peek
```

# SortedList

[[SortedList]]
[sorted list documentation](https://grantjenks.com/docs/sortedcontainers/introduction.html#sorted-list)

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

![[heapq]]