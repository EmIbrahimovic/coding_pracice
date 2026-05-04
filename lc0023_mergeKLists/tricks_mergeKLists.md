---
strongly-connected:
  - "[[tricks_mergeTwoLists]]"
  - "[[divide and conquer]]"
  - "[[priority queue]]"
tags: problem
---

# LeetCode 21. mergeKLists

## approach lessons

two cool approaches:
* [[priority queue]]
	* keep the heads of k lists in pq
	* pop and put into new list. chop off the head of that list
	* runtime $O(\log k \cdot n)$
* [[divide and conquer]] with [[tricks_mergeTwoLists]]
	* made a mistake in calculating the runtime here
	* if you set up a recurrence, you realize it's $O(\log k \cdot \sum_i n_i)$ and not $O(\sum_i n_i)$

## cpp optimizations


### py lessons

to put ListNode in heapq, use 
```
setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
```
