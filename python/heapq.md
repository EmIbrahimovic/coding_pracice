---
strongly-connected:
  - "[[python]]"
  - "[[python collections]]"
---


# heapq

https://docs.python.org/3/library/heapq.html

> For **min-heaps**, this implementation uses lists for which `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` for all _k_ for which the compared elements exist. Elements are counted from zero. The interesting property of a min-heap is that its smallest element is always the root, `heap[0]`.

add `_max` to function names to make it a max-heap

**heapq.heapify(_x_)[](https://docs.python.org/3/library/heapq.html#heapq.heapify "Link to this definition")**

**heapq.heappush(_heap_, _item_)[](https://docs.python.org/3/library/heapq.html#heapq.heappush "Link to this definition")**

**heapq.heappop(_heap_)[](https://docs.python.org/3/library/heapq.html#heapq.heappop "Link to this definition")**
> Pop and return the smallest item from the _heap_, maintaining the min-heap invariant. If the heap is empty, [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") is raised. To access the smallest item without popping it, use `heap[0]`.

**heapq.heappushpop(_heap_, _item_)[](https://docs.python.org/3/library/heapq.html#heapq.heappushpop "Link to this definition")**
> Push _item_ on the heap, then pop and return the smallest item from the _heap_. The combined action runs more efficiently than [`heappush()`](https://docs.python.org/3/library/heapq.html#heapq.heappush "heapq.heappush") followed by a separate call to [`heappop()`](https://docs.python.org/3/library/heapq.html#heapq.heappop "heapq.heappop").

## tips

```python
setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
```